from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockMovement

@receiver(post_save, sender=StockMovement)
def update_product_stock(sender, instance, created, **kwargs):
    """
    Sempre que uma movimentação for salva, atualiza o saldo do produto.
    """
    if created:
        product = instance.product
        if instance.type == 'IN':
            product.current_stock += instance.quantity
        elif instance.type == 'OUT':
            product.current_stock -= instance.quantity
        elif instance.type == 'ADJ':
            product.current_stock = instance.quantity
        
        product.save()