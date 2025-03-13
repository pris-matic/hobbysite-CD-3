from django.urls import path
from .views import article_categories_list, article

urlpatterns = [
    path('blog/articles/', article_categories_list, name='blog_categories'),
    path('blog/article/<int:key>/', article, name='article'),
]

app_name = 'blog'