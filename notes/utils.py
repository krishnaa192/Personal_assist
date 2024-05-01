import requests
from django.conf import settings

def fetch_youtube_video_details(video_id):
    """
    Fetch details for a specific YouTube video by its ID.
    Returns the video's title and other information.
    """
    api_key = settings.YOUTUBE_API_KEY
    base_url = 'https://www.googleapis.com/youtube/v3/videos'
    params = {
        'part': 'snippet',
        'id': video_id,
        'key': api_key,
    }
    response = requests.get(base_url, params=params)

    video_details = response.json().get('items', [])

    if video_details:
        # Extract the video title and other snippet information
        snippet = video_details[0]['snippet']
        video_title = snippet['title']
        video_description = snippet.get('description', 'No description available.')
        return {
            'title': video_title,
            'description': video_description,
            'snippet': snippet,
        }
    else:
        # Fallback if the video ID is invalid or there's no response
        return {
            'title': f"Video {video_id}",
            'description': 'No information available.',
            'snippet': {},
        }
