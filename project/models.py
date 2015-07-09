from django.db import models
from member.models import *

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    download = models.FileField(upload_to='projects_downloads')
    screenshot = models.ImageField(upload_to='projects_screenshots')
    members = models.ManyToManyField(Member)
