from django.shortcuts import render
from .models import ArticleCategory

# Create your views here.

def article_categories_list(request):
    categories = ArticleCategory.objects.all()
    return render(request, 'categories_list.html', {'categories': categories})