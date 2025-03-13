from django.shortcuts import render
from .models import ArticleCategory, Article

# Create your views here.

def article_categories_list(request):
    categories = ArticleCategory.objects.all()
    return render(request, 'categories_list.html', {'categories': categories})

def article(request, key):
    article = Article.objects.get(id=key)
    return render(request, 'article.html', {'article': article})