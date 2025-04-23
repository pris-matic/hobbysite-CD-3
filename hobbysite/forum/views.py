from django.shortcuts import render
from .models import ThreadCategory, Thread, Comment
from django.contrib.auth.decorators import login_required
from .forms import ThreadCategoryForm, ThreadForm, CommentForm

def get_forum_categories(request):
    items = ThreadCategory.objects.prefetch_related('post_set').all()
    return render(request,"forum/threads.html", {'categories': items})

def get_forum_thread(request,num):
    thread = Thread.objects.get(id=num)
    return render(request,"forum/specificThread.html",{'thread': thread})

@login_required
def create_thread(request):
    return 1

@login_required
def update_thread(request):
    return 2
