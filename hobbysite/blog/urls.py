from django.urls import path
from .views import article_categories_list, article

urlpatterns = [
    path('articles/', article_categories_list, name='blog_categories'),
    path('article/<int:key>/', article, name='article'),
]

app_name = 'blog'
