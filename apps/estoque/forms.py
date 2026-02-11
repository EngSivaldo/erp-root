from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'price', 'current_stock', 'is_active']
        
    def __init__(self, *args, **kwargs):
        # Recebemos o tenant para filtrar as categorias
        self.tenant = kwargs.pop('tenant', None)
        super().__init__(*args, **kwargs)
        
        # Filtra categorias apenas deste Tenant
        if self.tenant:
            self.fields['category'].queryset = Category.objects.filter(tenant=self.tenant)

        # Estilização Dark Mode
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'block w-full px-3 py-2 bg-slate-800 border border-slate-600 rounded-lg text-white focus:ring-emerald-500'
            })