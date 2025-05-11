from django.shortcuts import render, redirect
from .models import ThreadCategory, Thread, Comment
from django.contrib.auth.decorators import login_required
from .forms import ThreadCategoryForm, ThreadForm, CommentForm
from user_management.models import Profile
from django.db import IntegrityError

def get_forum_categories(request):
    items = ThreadCategory.objects.prefetch_related('thread_set').all()

    user_threads = []
    other_threads = []

    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
        user_threads = Thread.objects.filter(author=profile)
        other_threads = Thread.objects.exclude(author=profile)
    else:
        other_threads = Thread.objects.all()

    thread_map = {}

    for thread in other_threads:
        category_id = thread.category_id
        if category_id not in thread_map:
            thread_map[category_id] = []
        thread_map[category_id].append(thread)

    for category in items:
        if category.id in thread_map:
            category.threads = thread_map[category.id]
        else:
            category.threads = []

    return render(request,"forum/threads.html", {'categories': items, 'user_threads':user_threads})

def get_forum_thread(request,num):
    specific_thread = Thread.objects.get(id=num)
    related_threads = Thread.objects.filter(category=specific_thread.category).exclude(id=specific_thread.id)
    comments = Comment.objects.filter(thread=specific_thread)
    profile = None

    comment_form = None

    if request.user.is_authenticated:

        profile = Profile.objects.get(user=request.user)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.thread = specific_thread
                comment.author = Profile.objects.get(user=request.user)
                comment.save()
                return redirect('forum:get_forum_thread',num=specific_thread.id)
        
        else:
            comment_form = CommentForm()

    return render(request,"forum/specificThread.html",{'thread': specific_thread, 'comments': comments, 'comment': comment_form, 'profile':profile, 'related_threads':related_threads})

@login_required
def create_thread(request):

    if request.method == 'POST':
        category_form = ThreadCategoryForm(request.POST)
        thread_form = ThreadForm(request.POST, request.FILES)
    
        if category_form.is_valid():
            try:
                category = category_form.save(commit=False)

                if ThreadCategory.objects.filter(name__iexact=category.name).exists():
                    category_form.add_error(None,'Category already exists.')

                else:
                    category.save()
                    return redirect('forum:create_thread')

            except IntegrityError:
                category_form.add_error(None,'Category already exists.')

        if thread_form.is_valid():
            try:
                thread = thread_form.save(commit=False)
                profile = Profile.objects.get(user = request.user)
                thread_name = thread_form.cleaned_data.get('title')

                if Thread.objects.filter(title__iexact=thread_name, author=profile,category=thread.category).exists():
                    thread_form.add_error(None,'Thread already exists.')
                else:
                    thread.author = profile
                    thread.save()
                    return redirect('forum:get_forum_categories')
                
            except IntegrityError:
                thread_form.add_error(None,'Thread already exists.')

    else:
        category_form = ThreadCategoryForm()
        thread_form = ThreadForm()

    return render(request,"forum/createThread.html", {'category':category_form , 'thread':thread_form})

@login_required
def update_thread(request,num):

    thread= Thread.objects.get(id=num)

    if request.method == 'POST':
        thread_form = ThreadForm(request.POST, request.FILES, instance=thread)

        if thread_form.is_valid():
            updated_thread = thread_form.save(commit=False)
            profile = Profile.objects.get(user = request.user)
    
            updated_thread.author = profile
            updated_thread.save()
            return redirect('forum:get_forum_thread', num)
    
    else:
        thread_form = ThreadForm(instance=thread)      
    
    return render(request,"forum/updateThread.html", {'update_thread':thread_form})
