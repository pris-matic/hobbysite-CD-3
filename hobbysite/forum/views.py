from django.shortcuts import render
from .models import PostCategory

# Create your views here.

def getForumCategories(request):
    items = PostCategory.objects.prefetch_related('post_set').all()
    return render(request,"threads.html", {'categories': items})

def getForumThread(request,num):
    return render(request,"specificThread.html",{'num':num})