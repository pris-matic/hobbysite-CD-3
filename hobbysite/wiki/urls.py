from django.urls import path
from .views import articles_list, article_detail, article_create, article_update

urlpatterns = [
        path('articles/', articles_list, name='articles_list'),
        path('article/<int:key>/', article_detail, name='article_detail'),
        path('article/create/', article_create, name='article_create'),
        path('article/<int:key>/edit/', article_update, name='article_update'),
        ]

app_name = 'wiki'
