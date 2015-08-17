from django.shortcuts import render
from django.http import Http404
from blog.models import Article

def index(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'articles': articles})


def show(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        return render(request, 'blog/show.html', {'article': article})
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
