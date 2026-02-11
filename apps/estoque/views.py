from django.shortcuts import render
from .models import Product

def product_list(request):
    # Por enquanto pegamos todos, no futuro filtraremos pelo Tenant
    products = Product.objects.all()
    return render(request, 'estoque/product_list.html', {'products': products})