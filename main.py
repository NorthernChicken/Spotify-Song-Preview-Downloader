import requests
import json
from urllib.request import urlretrieve
import os

api_base_token = "https://accounts.spotify.com/api/"
api_base = "https://api.spotify.com/v1/"
try:
    artist_id = str(input("Enter the Spotify song ID: "))
except Exception as e:
    print(f"Invalid song ID. Error: {e}")

def get_access_token(api_base):
    api_url = api_base + "token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": "d88833f6ded1440d9fa7cf0ad3e4363f",
        "client_secret": "857b27f4d08b4a93a87fcae447934168"
    }

    response = requests.post(api_url, headers=headers, data=data)

    with open("access-token.json", "w") as file:
        json.dump(response.json(), file, indent=4)
    with open("access-token.json") as file:
        access_token_data = json.load(file)
    access_token = access_token_data["access_token"]
    return access_token

token = get_access_token(api_base_token)

def download_song(api_base, token, artist_id):
    api_url = api_base + "tracks/" + artist_id
    headers = {
        "Authorization": "Bearer " + token
    }

    response = requests.get(api_url, headers=headers)
    with open("results.json", "w") as file:
        json.dump(response.json(), file, indent=4)
    with open("results.json") as file:
        results_json = json.load(file)
    
    if "preview_url" in results_json:
        preview_url = results_json["preview_url"]
        urlretrieve(preview_url, "preview.mp3")
    else:
        print("Could not retreive that song.")

def clear_cache():
    root_dir = os.getcwd()
    path = os.path.join(root_dir, "access-token.json")
    os.remove(path)
    path = os.path.join(root_dir, "results.json")
    os.remove(path)

download_song(api_base, token, artist_id)
clear_cache()