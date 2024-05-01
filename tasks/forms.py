from django.forms.widgets import HiddenInput
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'deadline', 'category']
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
      