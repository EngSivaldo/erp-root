from django.contrib import admin
from django.urls import path, include
from core.views import home  # Importe a home aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # Rota para a página inicial
    path('estoque/', include('estoque.urls')),
]