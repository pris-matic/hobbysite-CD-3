from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def articles_list(request):
    return HttpResponse("Hello World. Wiki article list will go here")

def article_detail(request, pk = 1):
    return HttpResponse("Hello World. Wiki article detail will go here")
