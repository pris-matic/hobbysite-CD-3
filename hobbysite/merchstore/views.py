from .models import ProductType, Product
from django.shortcuts import render

def items_list(request):
    items = ProductType.objects.all()
    return render(request,"items_list.html", {'items': items})

def item_details(request, id):
    item = Product.objects.get(id=id)
    return render(request,"item_details.html", {'item': item})