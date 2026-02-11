import uuid
from django.db import models
from core.models import TenantModel  # Nossa base para multi-tenancy

class Category(TenantModel):
    name = models.CharField("Nome da Categoria", max_length=100)
    description = models.TextField("Descrição", blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name

class Product(TenantModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    name = models.CharField("Nome do Produto", max_length=255)
    sku = models.CharField("SKU/Código", max_length=50, help_text="Código único de inventário")
    price = models.DecimalField("Preço de Venda", max_digits=10, decimal_places=2)
    current_stock = models.DecimalField("Estoque Atual", max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        unique_together = ('tenant', 'sku') # SKU único por empresa

    def __str__(self) -> str:
        return f"{self.sku} - {self.name}"

class StockMovement(TenantModel):
    TYPE_CHOICES = (
        ('IN', 'Entrada'),
        ('OUT', 'Saída'),
        ('ADJ', 'Ajuste/Inventário'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="movements")
    quantity = models.DecimalField("Quantidade", max_digits=10, decimal_places=2)
    type = models.CharField("Tipo", max_length=3, choices=TYPE_CHOICES)
    reason = models.CharField("Motivo", max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Movimentação de Estoque"
        verbose_name_plural = "Movimentações de Estoque"