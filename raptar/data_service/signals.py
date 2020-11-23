from django.db.models.signals import post_save
from django.dispatch import receiver

from raptar.data_service.models.product import Product
from raptar.data_service.rules import ProductBusinessRule

@receiver(post_save, sender=Product)
def execute_product_business_rules(sender, instance, **kwargs):
    ProductBusinessRule.run_all(instance)