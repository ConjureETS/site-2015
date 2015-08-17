from django.shortcuts import render
from blog.models import *

def index(request):
	articles = Article.objects.all
	return render(request, 'blog/index.html', {'articles':articles})
