from django.shortcuts import render
from .models import ArticleCategory, Article
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def article_categories_list(request):
    categories = ArticleCategory.objects.all()
    return render(request, 'blog/blogArticlesList.html', {'categories': categories})

def article(request, key):
    article = Article.objects.get(id=key)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user.profile
            comment_form.instance.article = Article.objects.get(id=key)
            comment_form.save()

    ctx = {'article':article, 'comment_form':comment_form}
    return render(request, 'blog/blogArticle.html', ctx)
