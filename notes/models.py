from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    topic= models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(blank=True, null=True)
    #caan ulpoad multiple files
    files = models.FileField(upload_to='note/files/', blank=True, null=True)
    note_refference = models.CharField(max_length=100, blank=True, null=True)

    


    def __str__(self):
        return self.title
    
class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name