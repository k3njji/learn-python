import streamlit as st
import requests
import base64
import urllib.parse

st.set_page_config(page_title="Simple Social", layout="wide")

API_BASE_URL = "http://127.0.0.1:8089"

# Initialize session state
if "token" not in st.session_state:
    st.session_state.token = None

if "user" not in st.session_state:
    st.session_state.user = None


def get_headers():
    """Return Authorization header."""
    if st.session_state.token:
        return {
            "Authorization": f"Bearer {st.session_state.token}"
        }
    return {}


def login_page():
    st.title("🚀 Welcome to Simple Social")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if not email or not password:
        st.info("Enter your email and password above.")
        return

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login", type="primary", use_container_width=True):
            try:
                login_response = requests.post(
                    f"{API_BASE_URL}/auth/jwt/login",
                    data={
                        "username": email,
                        "password": password,
                    },
                    headers={
                        "Content-Type": "application/x-www-form-urlencoded"
                    },
                )

                if login_response.status_code != 200:
                    st.error("Invalid email or password.")
                    return

                token_data = login_response.json()
                st.session_state.token = token_data["access_token"]

                # FIXED: /user/me (not /users/me)
                user_response = requests.get(
                    f"{API_BASE_URL}/user/me",
                    headers=get_headers(),
                )

                if user_response.status_code == 200:
                    st.session_state.user = user_response.json()
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.session_state.token = None
                    st.error(
                        f"Failed to get user info: "
                        f"{user_response.status_code} - {user_response.text}"
                    )

            except requests.RequestException as e:
                st.error(f"Connection error: {e}")

    with col2:
        if st.button("Sign Up", use_container_width=True):
            try:
                signup_response = requests.post(
                    f"{API_BASE_URL}/auth/register",
                    json={
                        "email": email,
                        "password": password,
                    },
                )

                if signup_response.status_code == 201:
                    st.success("Account created successfully! Please log in.")
                else:
                    try:
                        error_detail = signup_response.json().get(
                            "detail",
                            signup_response.text,
                        )
                    except Exception:
                        error_detail = signup_response.text

                    st.error(f"Registration failed: {error_detail}")

            except requests.RequestException as e:
                st.error(f"Connection error: {e}")


def upload_page():
    st.title("📸 Share Something")

    uploaded_file = st.file_uploader(
        "Choose media",
        type=["png", "jpg", "jpeg", "mp4", "avi", "mov", "mkv", "webm"],
    )

    caption = st.text_area(
        "Caption",
        placeholder="What's on your mind?",
    )

    if uploaded_file and st.button("Share", type="primary"):
        try:
            with st.spinner("Uploading..."):
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type,
                    )
                }

                data = {"caption": caption}

                response = requests.post(
                    f"{API_BASE_URL}/upload",
                    files=files,
                    data=data,
                    headers=get_headers(),
                )

                if response.status_code == 200:
                    st.success("Posted successfully!")
                    st.rerun()
                else:
                    st.error(
                        f"Upload failed: "
                        f"{response.status_code} - {response.text}"
                    )

        except requests.RequestException as e:
            st.error(f"Connection error: {e}")


def encode_text_for_overlay(text: str) -> str:
    if not text:
        return ""

    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    return urllib.parse.quote(encoded)


def create_transformed_url(
    original_url: str,
    transformation_params: str = "",
    caption: str = "",
) -> str:
    if caption:
        encoded_caption = encode_text_for_overlay(caption)
        transformation_params = (
            f"l-text,ie-{encoded_caption},"
            f"ly-N20,lx-20,fs-40,co-white,"
            f"bg-000000A0,l-end"
        )

    if not transformation_params:
        return original_url

    parts = original_url.split("/")
    base_url = "/".join(parts[:4])
    file_path = "/".join(parts[4:])

    return f"{base_url}/tr:{transformation_params}/{file_path}"


def feed_page():
    st.title("🏠 Feed")

    try:
        response = requests.get(
            f"{API_BASE_URL}/feed",
            headers=get_headers(),
        )

        if response.status_code != 200:
            st.error(
                f"Failed to load feed: "
                f"{response.status_code} - {response.text}"
            )
            return

        posts = response.json()["posts"]

        if not posts:
            st.info("No posts yet! Be the first to share something.")
            return

        for post in posts:
            st.markdown("---")

            col1, col2 = st.columns([5, 1])

            with col1:
                st.markdown(
                    f"**{post['email']}** • "
                    f"{post['created_at'][:19].replace('T', ' ')}"
                )

            with col2:
                if post.get("is_owner", False):
                    if st.button(
                        "🗑️",
                        key=f"delete_{post['id']}",
                        help="Delete post",
                    ):
                        delete_response = requests.delete(
                            f"{API_BASE_URL}/posts/{post['id']}",
                            headers=get_headers(),
                        )

                        if delete_response.status_code == 200:
                            st.success("Post deleted.")
                            st.rerun()
                        else:
                            st.error(
                                f"Delete failed: "
                                f"{delete_response.text}"
                            )

            caption = post.get("caption", "")

            if post["file_type"] == "image":
                image_url = create_transformed_url(
                    post["url"],
                    caption=caption,
                )
                st.image(image_url, width=500)

            else:
                video_url = create_transformed_url(
                    post["url"],
                    "w-800,h-450,c-pad_resize,bg-blurred",
                )
                st.video(video_url)
                if caption:
                    st.caption(caption)

    except requests.RequestException as e:
        st.error(f"Connection error: {e}")


# Main App
if st.session_state.user is None:
    login_page()
else:
    st.sidebar.title(
        f"👋 {st.session_state.user['email']}"
    )

    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.session_state.user = None
        st.rerun()

    page = st.sidebar.radio(
        "Navigation",
        ["🏠 Feed", "📸 Upload"],
    )

    if page == "🏠 Feed":
        feed_page()
    else:
        upload_page()