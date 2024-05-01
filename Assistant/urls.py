
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),  # Auth URLs provided by django-allauth
    path('fun/', include('fun.urls')),  # Include fun app URLs
    path('tasks/', include('tasks.urls')),  # Include tasks app URLs
    path('notes/', include('notes.urls')),  # Include notes app URLs
    #ckeditor

    path('ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.browse, name='ckeditor_browse'),
]
#add static config 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
