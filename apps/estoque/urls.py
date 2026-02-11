from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/novo/', views.product_upsert, name='product_create'),
    path('produtos/editar/<uuid:pk>/', views.product_upsert, name='product_edit'),
    path('produtos/excluir/<uuid:pk>/', views.product_delete, name='product_delete'),
]