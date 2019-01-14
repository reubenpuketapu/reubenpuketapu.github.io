import json
import my_playlists


def hello(event, context):

    response = {
        "statusCode": 200,
        "body": my_playlists.getPlaylistTracks()
    }

    return response


print(hello('', ''))
