from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm, TransactionForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore/product_form.html'
    success_url = reverse_lazy('product_list')

    def get_form(self):
        form = super().get_form()
        form.fields['owner'].disabled = True
        return form

    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.stock == 0:
            instance.status = 'Out of stock'
        else:
            instance.status = 'Available'
        instance.save()
        return super().form_valid(form)