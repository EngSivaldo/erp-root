from django.contrib import admin
from .models import Category, Product, StockMovement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'tenant')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'current_stock', 'tenant')
    search_fields = ('name', 'sku')

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'type', 'quantity', 'date', 'tenant')