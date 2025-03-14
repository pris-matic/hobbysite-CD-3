from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleCategory

# Create your views here.

def articles_list(request):
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    return render(request, 'wiki/articles_list.html', {'categories':categories, 'articles':articles})

def article_detail(request, key):
    article = Article.objects.get(id=key)
    return render(request, '', {'article': article})
