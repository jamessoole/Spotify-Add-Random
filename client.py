import random
import string
import urllib
import requests

class SpotifyClient(object):
    # constructor
    # self denotes this instance
    def __init__(self, api_key):
        self.api_key = api_key
    

    def get_tracks(self):
        # reference  https://developer.spotify.com/console/get-search-item/
        # search for tracks w/ given query and rand offset
        
        # get a random lowercase letter in middle of wildcard values
        # formats the wildcard to be used in a url, i.e turn % into %25 (the url code for it)
        # random no. for first item
        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)
        limit = input("How many songs do you want to add (max 50)?")

        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track&limit={limit}'
        
        # make a request
        response = requests.get(
            url,
            headers = {
                # response should be json
                "Content-Type" : "application.json", 
                # is authorized b/c u have an api key
                "Authorization" : f"Bearer {self.api_key}"
            }
        )
        # parse response as json
        response_json = response.json()
        if ('error' in response_json):
            print(f"There has been an Error: {response_json['error']}")

        tracks = [ track for track in response_json['tracks']['items'] ]
        print(f'Found {len(tracks)} tracks')
        return tracks


    
    def add_tracks_to_library(self, track_ids):
        url = 'https://api.spotify.com/v1/me/tracks'
        response = requests.put(
            url,
            headers = {
                "Content-Type" : "application.json", 
                "Authorization" : f"Bearer {self.api_key}"
            },
            # what we want to add
            json = {
                "ids" : track_ids
            }
        )
        # check if response worked (200)
        return response.ok