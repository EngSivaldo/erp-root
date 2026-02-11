from django.urls import path
from .views import product_list

app_name = 'estoque'

urlpatterns = [
    path('produtos/', product_list, name='product_list'),
]