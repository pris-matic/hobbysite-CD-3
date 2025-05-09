from django.urls import path
from .views import article_categories_list, article, article_create, article_update

urlpatterns = [
    path('articles/', article_categories_list, name='blog_categories'),
    path('article/<int:key>/', article, name='article'),
    path('article/add/', article_create, name='article_create'),
    path('article/<int:key>/edit', article_update, name='article_update')
]

app_name = 'blog'
