from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json


def getPlaylistTracks():
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    uri = 'spotify:user:1242159109:playlist:1nvtKCnoaRCFpSDT9zLpAF'
    username = uri.split(':')[2]
    playlist_id = uri.split(':')[4]

    results = sp.user_playlist(username, playlist_id)
    return json.dumps(results)
