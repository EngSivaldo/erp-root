from django.contrib import admin
from django.urls import path, include
# Se 'core' estiver dentro de 'apps', use:
# from apps.core.views import home 
# Se estiver na raiz:
try:
    from core.views import home
except ImportError:
    from apps.core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('estoque/', include('estoque.urls')),
]