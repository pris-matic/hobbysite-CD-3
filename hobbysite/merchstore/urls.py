from django.urls import path
from . import views

urlpatterns = [
    path('items', views.product_list_view, name='product_list'),
    path('item/<int:pk>', views.product_detail_view, name='product_detail'),
    path('item/add', views.product_create_view, name='product_add'),
    path('item/<int:pk>/edit', views.product_update_view, name='product_update'),
    path('cart', views.cart_view, name='cart'),
    path('transactions', views.transaction_list_view, name='transactions'),
]

app_name= 'merchstore'
