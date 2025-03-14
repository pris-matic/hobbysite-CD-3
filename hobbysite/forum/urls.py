from django.urls import path
from .views import get_forum_categories, get_forum_thread

urlpatterns = [
    path('forum/threads/',get_forum_categories, name= 'get_forum_categories'),
    path('forum/thread/<int:num>/',get_forum_thread, name='get_forum_thread'),
]

app_name = 'forum'