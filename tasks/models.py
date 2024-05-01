from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created']

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed', '-created']
        