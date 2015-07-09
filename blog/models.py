from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='article_photos')
