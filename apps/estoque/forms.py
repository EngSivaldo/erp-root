from django import 
from .models import Product

class ProductForm(django.forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'price', 'stock_quantity', 'description']
        widgets = {
            # Estilização Senior com Tailwind diretamente no Form
            field: django.forms.TextInput(attrs={'class': 'block w-full px-3 py-2 bg-slate-800 border border-slate-600 rounded-lg text-white focus:ring-emerald-500'})
            for field in ['name', 'sku']
        }