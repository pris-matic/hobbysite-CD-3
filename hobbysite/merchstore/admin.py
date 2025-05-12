from django.contrib import admin
from .models import ProductType, Product, Transaction

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ('name', 'description')
    ordering = ('name',)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'product_type', 'owner', 'price', 'stock', 'status')
    list_filter = ('status', 'product_type')
    search_fields = ('name', 'description', 'owner__display_name')

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('product', 'buyer', 'amount', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ('product__name', 'buyer__display_name')

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)