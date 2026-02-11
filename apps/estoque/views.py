from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

@login_required
def product_list(request):
    # Filtra produtos pelo tenant do usuário logado
    products = Product.objects.filter(tenant=request.user.tenant).order_by('-id')
    return render(request, 'estoque/product_list.html', {'products': products})

@login_required
def product_upsert(request, pk=None):
    # Busca o produto ou retorna None (para criação)
    product = get_object_or_404(Product, pk=pk, tenant=request.user.tenant) if pk else None
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product, tenant=request.user.tenant)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.tenant = request.user.tenant
            obj.save()
            
            # Retorna apenas a tabela para o HTMX atualizar a lista
            products = Product.objects.filter(tenant=request.user.tenant).order_by('-id')
            return render(request, 'estoque/partials/product_table.html', {'products': products})
    else:
        form = ProductForm(instance=product, tenant=request.user.tenant)
    
    return render(request, 'estoque/partials/product_form_modal.html', {'form': form, 'product': product})

@login_required
def product_delete(request, pk):
    # Esta é a função que o erro dizia que estava faltando
    product = get_object_or_404(Product, pk=pk, tenant=request.user.tenant)
    
    if request.method == 'DELETE':
        product.delete()
        # Retorna vazio para o HTMX remover a linha da tabela
        return HttpResponse("")
    
    return HttpResponse(status=405)