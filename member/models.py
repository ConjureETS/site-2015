from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="members", blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    position = models.CharField(max_length=50, blank=True, null=True)
