import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# =========================
# ENV SETUP
# =========================
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# 🔥 MUST match Spotify dashboard EXACTLY
REDIRECT_URI = "http://127.0.0.1:5555/callback/"

# =========================
# SCRAPE BILLBOARD
# =========================
def scrape_songs():
    URL = "https://www.billboard.com/charts/hot-100/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # ✅ robust selector
    song_elements = soup.select("li ul li h3")

    songs = [song.get_text(strip=True) for song in song_elements]

    print(f"🎵 Scraped {len(songs)} songs")
    return songs[:12]


# =========================
# SPOTIFY AUTH
# =========================
def get_spotify_client():
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope="playlist-modify-private",
            cache_path=".spotify_cache",   # avoid old cache issues
            show_dialog=True               # 🔥 FORCE permission screen
        )
    )


# =========================
# SEARCH SONGS
# =========================
def search_songs(sp, songs):
    uris = []

    for song in songs:
        result = sp.search(q=f"track:{song}", type="track", limit=1)

        try:
            uri = result["tracks"]["items"][0]["uri"]
            uris.append(uri)
        except IndexError:
            print(f"❌ Not found: {song}")

    print(f"✅ Found {len(uris)} songs on Spotify")
    return uris


# =========================
# CREATE PLAYLIST
# =========================
def create_playlist(sp, uris):
    user_id = sp.current_user()["id"]

    playlist = sp.user_playlist_create(
        user=user_id,
        name="Billboard Hot 100 (Auto)",
        public=False
    )

    sp.playlist_add_items(
        playlist_id=playlist["id"],
        items=uris
    )

    print("🎉 Playlist created!")
    print("🔗", playlist["external_urls"]["spotify"])


# =========================
# MAIN
# =========================
def main():
    # 🔥 debug (optional)
    print("Using redirect:", REDIRECT_URI)

    songs = scrape_songs()

    sp = get_spotify_client()

    # confirm user + scope
    print("👤 User:", sp.current_user()["id"])
    print("🔑 Scope:", sp.auth_manager.scope)

    uris = search_songs(sp, songs)

    create_playlist(sp, uris)


# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()