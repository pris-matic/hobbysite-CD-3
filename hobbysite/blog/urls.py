from django.urls import path
from .views import article_categories_list

urlpatterns = [
    path('blog/categories/', article_categories_list, name='blog_categories'),
]

app_name = 'blog'