import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Optional

class Tenant(models.Model):
    """
    Representa a 'Empresa' ou 'Conta' que utiliza o ERP.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nome da Empresa", max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name = "Empresas"

    def __str__(self) -> str:
        return self.name

class CustomUser(AbstractUser):
    """
    Usuário customizado que pertence a um Tenant.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(
        Tenant, 
        on_delete=models.CASCADE, 
        related_name="users",
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class TenantModel(models.Model):
    """
    Classe base Abstrata para todos os modelos que devem ser filtrados por Tenant.
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True