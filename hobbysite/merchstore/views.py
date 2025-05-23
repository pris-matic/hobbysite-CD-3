from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Transaction
from .forms import ProductForm, TransactionForm

def product_list_view(request):
    all_products = Product.objects.all()
    user_products = []
    if request.user.is_authenticated:
        profile = request.user.profile
        user_products = all_products.filter(owner=profile)
        all_products = all_products.exclude(owner=profile)

    return render(request, 'merchstore/productList.html', {
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
                return redirect('merchstore:cart')

    return render(request, 'merchstore/productDetail.html', {
        'product': product,
        'form': form,
        'is_owner': is_owner,
    })

@login_required
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user.profile
            product.save()
            return redirect('merchstore:product_list')
    return render(request, 'merchstore/productForm.html', {
        'form': form
    })

@login_required
def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.profile != product.owner:
        return redirect('merchstore:product_list')

    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.stock == 0:
                instance.status = 'Out of stock'
            else:
                instance.status = 'Available'
            instance.save()
            return redirect('merchstore:product_list')

    return render(request, 'merchstore/productForm.html', {
        'form': form
    })

@login_required
def cart_view(request):
    profile = request.user.profile
    transactions = Transaction.objects.filter(buyer=profile)
    grouped = {}
    for tx in transactions:
        owner = tx.product.owner if tx.product else None
        if owner:
            grouped.setdefault(owner, []).append(tx)
    return render(request, 'merchstore/cart.html', {
        'grouped_transactions': grouped
    })

@login_required
def transaction_list_view(request):
    profile = request.user.profile
    transactions = Transaction.objects.filter(product__owner=profile)
    grouped = {}
    for tx in transactions:
        buyer = tx.buyer
        if buyer:
            grouped.setdefault(buyer, []).append(tx)
    return render(request, 'merchstore/transactions.html', {
        'grouped_transactions': grouped
    })