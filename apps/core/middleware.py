import threading
from django.http import HttpRequest, HttpResponse
from typing import Callable, Optional  # Adicionado Optional aqui
from core.models import Tenant

# Thread-safe storage para o tenant atual
_thread_locals = threading.local()

def get_current_tenant() -> Optional[Tenant]:
    return getattr(_thread_locals, 'tenant', None)

class TenantMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            _thread_locals.tenant = getattr(request.user, 'tenant', None)
        else:
            _thread_locals.tenant = None

        response = self.get_response(request)
        
        # Limpa para evitar vazamento entre requests
        _thread_locals.tenant = None
        
        return response