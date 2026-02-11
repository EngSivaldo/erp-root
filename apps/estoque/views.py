from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'estoque/product_list.html', {'products': products})

# View para Criar/Editar (Híbrida)
def product_upsert(request, pk=None):
    product = get_object_or_404(Product, pk=pk) if pk else None
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            # Retorna apenas a lista atualizada via HTMX
            products = Product.objects.all().order_by('-id')
            return render(request, 'estoque/partials/product_table.html', {'products': products})
    
    form = ProductForm(instance=product)
    return render(request, 'estoque/partials/product_form_modal.html', {'form': form, 'product': product})

# View para Excluir
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'DELETE':
        product.delete()
        return HttpResponse("") # HTMX remove a linha ao receber vazio