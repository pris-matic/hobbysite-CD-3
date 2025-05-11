from django.urls import path
from .views import get_forum_categories, get_forum_thread, create_thread, update_thread

urlpatterns = [
    path('threads/',get_forum_categories, name='get_forum_categories'),
    path('thread/<int:num>/',get_forum_thread, name='get_forum_thread'),
    path('thread/add/',create_thread, name='create_thread'),
    path('thread/<int:num>/edit',update_thread,name='update_thread'),
]

app_name = 'forum'
