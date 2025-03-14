from .models import ProductType, Product
from django.shortcuts import render

def items_list(request):
    items = ProductType.objects.all()
    return render(request,"itemsList.html", {'items': items})

def item_details(request, item_id):
    item = Product.objects.get(id=item_id)
    return render(request,"itemDetails.html", {'item': item})