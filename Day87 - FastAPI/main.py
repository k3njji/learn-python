from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

app = FastAPI()

engine = create_engine(
    'sqlite:///C:/Python by Angela Yu/Day87 - FastAPI/users.db',
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True

class UserUpdateName(BaseModel):
    name: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return 'hello world'

# get 1 user
@app.get('/users/{user_id}', response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='user not found')
    return user

# get all users
@app.get('/users', response_model = list[UserResponse])
def get_all_user(db: Session = Depends(get_db)):
    userss = db.query(User).all()
    return userss

# post
@app.post('/users', response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail='User already registered')

    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# update users
@app.put('/users/{user_id}', response_model=UserResponse)
def update_user(user_id: int, usr: UserUpdateName, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail='user does not exist')

    # update fields
    db_user.name = usr.name

    db.commit()
    db.refresh(db_user)

    return db_user

# delet users
@app.delete('delete/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code = 404, detail='not exist')
    
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
