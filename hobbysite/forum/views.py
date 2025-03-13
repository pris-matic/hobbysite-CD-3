from django.shortcuts import render
from .models import PostCategory, Post

# Create your views here.

def get_forum_categories(request):
    items = PostCategory.objects.prefetch_related('post_set').all()
    return render(request,"threads.html", {'categories': items})

def get_forum_thread(request,num):
    post = Post.objects.get(id=num)
    return render(request,"specificThread.html",{'thread': post})