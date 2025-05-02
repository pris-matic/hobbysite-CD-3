from django.shortcuts import render
from .models import Article, ArticleCategory

def articles_list(request):
    categories = ArticleCategory.objects.all()
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author__user=request.user)
    else: 
        user_articles = {}
    return render(request, 'wiki/articlesList.html', {'categories':categories, 'user_articles':user_articles})

def article_detail(request, key):
    return render(request, 'wiki/articleDetail.html', {'article': Article.objects.get(id=key)})
