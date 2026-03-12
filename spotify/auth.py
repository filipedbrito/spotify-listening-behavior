import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


load_dotenv()


def get_user_client():

    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="playlist-read-private"
    )

    return spotipy.Spotify(auth_manager=auth_manager)


def get_public_client():

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)

    return sp