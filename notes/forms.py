from django.forms.widgets import HiddenInput
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class VideoNotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['content', 'files','title','topic']

    
      