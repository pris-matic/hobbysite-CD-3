from django.shortcuts import render
from .models import PostCategory, Post

def get_forum_categories(request):
    items = PostCategory.objects.prefetch_related('post_set').all()
    return render(request,"forum/threads.html", {'categories': items})

def get_forum_thread(request,num):
    post = Post.objects.get(id=num)
    return render(request,"forum/specificThread.html",{'thread': post})
