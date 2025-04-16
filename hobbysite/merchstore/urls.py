from django.urls import path
from . import views

urlpatterns = [
    path('merchstore/items/', views.items_list, name='items_list'),
    path('merchstore/item/<int:item_id>/', views.item_details, name='item_details'),
]

app_name= 'merchstore'