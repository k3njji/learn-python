import os
import shutil
import tempfile
from contextlib import asynccontextmanager

from fastapi import FastAPI, File, UploadFile, Form, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import create_db_and_tables, get_async_session, Post, User
from app.images import imagekit
import uuid

from app.users import auth_backend, current_active_user, fastapi_users

from app.schemas import PostCreate, PostResponse, UserCreate, UserRead, UserUpdate

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix='/auth/jwt', tags=['auth'])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_reset_password_router(), prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_verify_router(UserRead), prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix='/user', tags=['user'])


# create
@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    temp_file_path = None

    try:
        suffix = os.path.splitext(file.filename)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        with open(temp_file_path, "rb") as f:
            file_data = f.read()

        upload_result = imagekit.files.upload(
            file=file_data,
            file_name=file.filename,
            tags=["backend-upload"],
            use_unique_file_name=True,
        )

        post = Post(
            user_id=user.id,
            caption=caption,
            url=upload_result.url,
            file_type=(
                "video"
                if file.content_type.startswith("video/")
                else "image"
            ),
            file_name=upload_result.name,
        )

        session.add(post)
        await session.commit()
        await session.refresh(post)

        return {
            'user_id':user.id,
            "id": post.id,
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat(),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

        await file.close()

# read
from sqlalchemy.orm import lazyload

@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    try:
        result = await session.execute(
            select(Post)
            .options(lazyload("*"))   # Disable automatic joined eager loading
            .order_by(Post.created_at.desc())
        )

        posts = result.scalars().all()

        result = await session.execute(
            select(User).options(lazyload("*"))
        )
        users = result.scalars().all()

        user_dict = {
            str(u.id): u.email
            for u in users
        }

        return {
            "posts": [
                {
                    "id": str(post.id),
                    "user_id": str(post.user_id),
                    "caption": post.caption,
                    "url": post.url,
                    "file_type": post.file_type,
                    "file_name": post.file_name,
                    "created_at": post.created_at.isoformat(),
                    "is_owner": str(post.user_id) == str(user.id),
                    "email": user_dict.get(
                        str(post.user_id),
                        "Unknown User"
                    ),
                }
                for post in posts
            ]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# update

# delete
@app.delete("/posts/{post_id}")
async def delete_post(
    post_id: str,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    try:
        post_uuid = uuid.UUID(post_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid post ID")

    result = await session.execute(
        select(Post).where(Post.id == post_uuid)
    )
    post = result.scalar_one_or_none()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to delete this post"
        )

    await session.delete(post)
    await session.commit()

    return {"message": "Post deleted successfully"}