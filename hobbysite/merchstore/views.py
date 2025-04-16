from .models import ProductType, Product
from django.shortcuts import render

def items_list(request):
    items = ProductType.objects.all()
    return render(request,"merchstore/itemsList.html", {'items': items})

def item_details(request, item_id):
    item = ProductType.objects.get(id=item_id)
    return render(request,"merchstore/itemDetails.html", {'item': item})
