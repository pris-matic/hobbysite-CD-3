from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import TransactionForm

def product_list_view(request):
    all_products = Product.objects.all()
    user_products = []
    if request.user.is_authenticated:
        profile = request.user.profile
        user_products = all_products.filter(owner=profile)
        all_products = all_products.exclude(owner=profile)

    return render(request, 'merchstore/product_list.html', {
        'user_products': user_products,
        'all_products': all_products,
    })

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = TransactionForm(request.POST or None)
    is_owner = request.user.is_authenticated and request.user.profile == product.owner

    if request.method == 'POST' and not is_owner:
        if not request.user.is_authenticated:
            return redirect('login')

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.product = product
            transaction.buyer = request.user.profile

            if product.stock >= transaction.amount:
                product.stock -= transaction.amount
                product.save()
                transaction.save()
                return redirect('cart')

    return render(request, 'merchstore/product_detail.html', {
        'product': product,
        'form': form,
        'is_owner': is_owner,
    })