from django.shortcuts import render, redirect
from .models import ArticleCategory, Article
from .forms import CommentForm, ArticleCreateForm
from django.contrib.auth.decorators import login_required

def article_categories_list(request):
    categories = ArticleCategory.objects.all()
    return render(request, 'blog/blogArticlesList.html', {'categories': categories})

def article(request, key):
    article = Article.objects.get(id=key)
    author_articles = Article.objects.filter(author=article.author).exclude(id=article.id)
    comments = article.comments.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user.profile
            comment_form.instance.article = Article.objects.get(id=key)
            comment_form.save()

    ctx = {'article':article, 'comment_form':comment_form, 'comments':comments, 'author_articles':author_articles}
    return render(request, 'blog/blogArticle.html', ctx)

@login_required
def article_create(request):
    article_form = ArticleCreateForm()
    if request.method == 'POST':
        article_form = ArticleCreateForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.instance.author = request.user.profile
            article = article_form.save()
            return redirect('blog:article', key=article.pk)

    ctx = {'article_form':article_form}
    return render(request, 'blog/blogArticleMaker.html', ctx)

@login_required
def article_update(request, key):
    article = Article.objects.get(id=key)
    if request.method == 'POST':
        article_form = ArticleCreateForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('blog:article', key=article.pk)
    else:
        article_form = ArticleCreateForm(instance=article)

    ctx = {'article_form':article_form}
    return render(request, 'blog/blogArticleUpdater.html', ctx)
