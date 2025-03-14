from django.shortcuts import render
from .models import ArticleCategory, Article

# Create your views here.

def article_categories_list(request):
    categories = ArticleCategory.objects.all()
    return render(request, 'blog/blogArticlesList.html', {'categories': categories})

def article(request, key):
    article = Article.objects.get(id=key)
    return render(request, 'blog/blogArticle.html', {'article': article})