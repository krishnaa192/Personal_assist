from django.urls import path
from . import views



urlpatterns = [
    path('', views.view_notes , name='notes'),
    path('videos/', views.search_youtube_videos, name='videos'),
     path('video/<str:video_id>/', views.video_notes, name='video_notes'),
]