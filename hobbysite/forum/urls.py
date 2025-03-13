from django.urls import path
from .views import get_forum_categories, get_forum_thread

urlpatterns = [
    path('forum/threads/',get_forum_categories, name= 'getForumCategories'),
    path('forum/thread/<int:num>/',get_forum_thread, name='getForumThread'),
]

app_name = 'forum'