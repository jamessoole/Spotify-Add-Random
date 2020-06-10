# Spotify Add Random Tracks

### Add multiple random tracks to user library using Spotify API.

Python script `run.py` calls `client.py`

##### To Use:
- get OAUTH token [here](https://developer.spotify.com/console/put-current-user-saved-tracks/)
- must register personal project
- set token w/ following on cmd line
- `export token=<paste token here>` on linux or `set token=<paste token here>` on windows
- optional `env | grep token` to check if token has loaded

###### Notes:
- Tokens expire after an hour
- `KeyError: 'tracks'` likely caused by expired token
- current syntax for python3 (f-strings)


