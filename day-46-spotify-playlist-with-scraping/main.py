from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


# constants
CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_URL = os.environ["SPOTIPY_REDIRECT_URI"]
USERNAME = "11135400611"


# strip song titles
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
site = requests.get(URL)

soup = BeautifulSoup(site.text, 'html.parser')
songs = soup.find_all(name='h3', class_="a-no-trucate")
artists = soup.find_all(name='span', class_="a-no-trucate")
song_titles = [song.getText().strip() for song in songs]
song_artists = [artist.getText().strip() for artist in artists]
artists_songs_dict = {song_artists[i]: song_titles[i] for i in range(len(song_titles))}


# spotify authentication
SCOPE = "playlist-modify-public"
token = SpotifyOAuth(scope=SCOPE, username=USERNAME)
sp = spotipy.Spotify(auth_manager=token)

# spotify create a playlist
playlist_name = f"Billboard top 100 for {date}"
created_playlist = sp.user_playlist_create(USERNAME, playlist_name, public=True, description="Automated playlist")
tracks_uris = []
for artist in artists_songs_dict:
    try:
        result = sp.search(q=f"{artist} {artists_songs_dict[artist]}", type="track")
        track_uri = result["tracks"]["items"][0]["uri"]
        tracks_uris.append(track_uri)
    except IndexError:
        continue


# adding the songs to the playlist
sp.user_playlist_add_tracks(user=USERNAME, playlist_id=created_playlist["id"], tracks=tracks_uris)