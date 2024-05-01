from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from .forms import *
import requests
from .utils import fetch_youtube_video_details


# Create your views here.
def view_notes(request):
    notes = Notes.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'notes/notes.html', context)  

def add_notes(request):
    return render(request, 'notes/add_notes.html')

def update_notes(request):
    return render(request, 'notes/update_notes.html')

def delete_notes(request):
    return render(request, 'notes/delete_notes.html')

def upload_notes(request):
    return render(request, 'notes/upload_notes.html')

def download_notes(request):
    return render(request, 'notes/download_notes.html')

def convert_to_pdf(request):
    return render(request, 'notes/convert_to_pdf.html')
# views.py

def search_youtube_videos(request):
    # Fetch the video details using the reusable function
    query = request.GET.get('q', 'Django')  # Default search query is "Django"

    # Example: Fetch 10 videos based on the search query
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 10,
        'key': settings.YOUTUBE_API_KEY,
    }

    response = requests.get(base_url, params=params)
    video_items = response.json().get('items', [])

    # Extract video details using the reusable function
    videos = [
        {
            'video_id': item['id']['videoId'],
            'title': fetch_youtube_video_details(item['id']['videoId'])['title'],
        }
        for item in video_items
    ]

    return render(request, 'notes/videos.html', {'videos': videos})


def video_notes(request, video_id):
    # Fetch the video details using the reusable function
    video_info = fetch_youtube_video_details(video_id)
    video_title = video_info['title']

    # Retrieve the user's notes for the specific video
    notes = Notes.objects.filter(note_refference=video_id, user=request.user).first()

    if request.method == 'POST':
        note_content = request.POST.get('note_content', '')

        if notes:
            # Update existing notes
            notes.content = note_content
            notes.save()
        else:
            # Create new notes
            Notes.objects.create(
                user=request.user,
                title=f'Notes for {video_title}',  # Use the video title
                topic=Topic.objects.first(),
                note_refference=video_id,
                content=note_content,
            )

        # Redirect to avoid POST duplication
        return redirect('video_notes', video_id=video_id)

    # Render the video notes form along with the video title
    return render(request, 'notes/video_notes.html', {
        'video_id': video_id,
        'video_title': video_title,
        'notes': notes,
    })