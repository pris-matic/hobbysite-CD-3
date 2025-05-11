from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, ArticleCategory
from .forms import ArticleForm, CommentForm

def articles_list(request):
    categories = ArticleCategory.objects.all()
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author__user=request.user)
    else: 
        user_articles = {}
    return render(request, 'wiki/articlesList.html', {'categories':categories, 'user_articles':user_articles})

def article_detail(request, key):
    article = Article.objects.get(id=key)
    more_in_category = Article.objects.filter(category=article.category).exclude(id=article.id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment_form.instance.author = request.user.profile
        comment_form.instance.article = article
        if comment_form.is_valid():
            comment_form.save()
            return redirect(reverse('wiki:article_detail', args=[article.pk]))

    else:
        comment_form = CommentForm()
    return render(request, 'wiki/articleDetail.html', {'article': article, 'more_in_category': more_in_category, 'comment_form': comment_form})

@login_required
def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        article_form.instance.author = request.user.profile
        if article_form.is_valid():
            article = article_form.save()
            return redirect(reverse('wiki:article_detail', args=[article.pk]))
        else:
            print(article_form.errors)
    else: 
        article_form = ArticleForm()
    return render(request, 'wiki/articleCreate.html', {'article_form': article_form})

@login_required
def article_update(request, key):
    article = get_object_or_404(Article, id=key)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect(reverse('wiki:article_detail', args=[article.pk]))
    else:
        article_form = ArticleForm(instance=article)
    
    return render(request, 'wiki/articleUpdate.html', {'article_form': article_form})

    
