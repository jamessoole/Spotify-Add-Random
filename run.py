import os
from client import SpotifyClient


# IMPORTANT - set token w/ following on cmd line
# export token=<paste token here>

# get OAUTH from https://developer.spotify.com/console/put-current-user-saved-tracks/
# optional - env | grep token     linux keywords to check if loaded
# note - export is linux command, use 'set' for windows

# note - Tokens expire after an hour
# KeyError: 'tracks' likely caused by expired token

# current syntax for python3 (f-strings)



def run():

    # # if you'd prefer an input
    # token = input("What's your OAUTH Token? ")
    # client = SpotifyClient(token)
    client = SpotifyClient(os.getenv('token'))
    print(f"token is: {os.getenv('token')}")

    #--search for random songs
    tracks = client.get_tracks()

    # get each track id
    track_ids = [track['id'] for track in tracks]
    
    #--add songs to library
    was_added_to_library = client.add_tracks_to_library(track_ids)
    if (was_added_to_library == True):
        for track in tracks:
            print(f"Added {track['name']} to your library")


    # # testing
    # for track in tracks:
    #     print(track['name'])


# if run directly
if __name__ == "__main__":
    run()