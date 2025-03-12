from django.urls import path
from .views import getForumCategories, getForumThread

urlpatterns = [
    path('forum/threads/',getForumCategories, name= 'getForumCategories'),
    path('forum/thread/<int:num>/',getForumThread, name='getForumThread'),
]

app_name = 'forum'