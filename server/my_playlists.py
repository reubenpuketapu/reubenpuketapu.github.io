from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import os


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


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
    return findYoutubeLink(track, artists)


def findYoutubeLink(track, artist):
    search = track + ' ' + ' '.join(artist)
    return search


def get():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "youtube_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="surfing"
    )
    response = request.execute()

    print(response)


print(getPlaylistTracks())
