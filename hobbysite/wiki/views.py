from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleCategory

# Create your views here.

def articles_list(request):
    categories = ArticleCategory.objects.all()
    return render(request, 'wiki/articles_list.html', {'categories':categories})

def article_detail(request, id):
    return render(request, 'wiki/article_detail.html', {'article': Article.objects.get(id=id)})
