from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PostCategory, Post

# Create your views here.

# @login_required
def getForumCategories(request):
    items = PostCategory.objects.prefetch_related('post_set').all()
    return render(request,"threads.html", {'categories': items})

def getForumThread(request,num):
    post = Post.objects.get(id=num)
    return render(request,"specificThread.html",{'thread': post})