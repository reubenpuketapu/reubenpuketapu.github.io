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
    output = list(
        map(mapSpotifyTrack, results['tracks']['items']))

    return json.dumps(output)


def mapSpotifyTrack(tracks):
    track = tracks['track']['name']

    artists = []
    for artist in tracks['track']['artists']:
        artists.append(artist['name'])

    image = tracks['track']['album']['images'][0]['url']
    return {'track': track, 'artists': artists, 'image': image, 'youtube': findYoutubeLink(track, artists)}


def findYoutubeLink(track, artist):
    search = track + ' ' + ' '.join(artist)
    return search
