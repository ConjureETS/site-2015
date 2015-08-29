from django.db import models
from member.models import *

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    download = models.FileField(upload_to='projects_downloads', null=True, blank=True)
    screenshot = models.ImageField(upload_to='projects_screenshots', null=True, blank=True)
    members = models.ManyToManyField(Member, null=True, blank=True)
