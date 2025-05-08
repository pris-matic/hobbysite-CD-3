from django.shortcuts import render, redirect, reverse
from .models import Article, ArticleCategory
from .forms import ArticleForm

def articles_list(request):
    categories = ArticleCategory.objects.all()
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author__user=request.user)
    else: 
        user_articles = {}
    return render(request, 'wiki/articlesList.html', {'categories':categories, 'user_articles':user_articles})

def article_detail(request, key):
    return render(request, 'wiki/articleDetail.html', {'article': Article.objects.get(id=key)})

def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.instance.author = request.user.profile
            article = article_form.save()
            return redirect(reverse('wiki:article_detail', args=[article.pk]))
        else:
            print(article_form.errors)
    else: 
        article_form = ArticleForm()
    return render(request, 'wiki/articleCreate.html', {'article_form': article_form})
    
