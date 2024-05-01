from django.shortcuts import render

# Create your views here.


# views.py

import requests

# def fetch_spotify_playlists(request):
#     access_token = request.user.socialaccount.token.token  # Get access token from authenticated user
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     response = requests.get("https://api.spotify.com/v1/me/playlists", headers=headers)
#     if response.status_code == 200:
#         playlists = response.json()['items']
#         return playlists
#     else:
#         # Handle error gracefully
#         return None

def home(request):
    return render(request, 'home.html')