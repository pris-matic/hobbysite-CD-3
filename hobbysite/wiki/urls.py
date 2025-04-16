from django.urls import path
from .views import articles_list, article_detail

urlpatterns = [
        path('wiki/articles/', articles_list, name='articles_list'),
        path('wiki/article/<int:key>/', article_detail, name='article_detail'),
        ]

app_name = 'wiki'
