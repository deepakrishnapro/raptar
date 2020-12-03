from django.db.models.signals import post_save
from django.dispatch import receiver

from raptar.data_service.models.testreport import TestReport
from raptar.data_service.rules.testreport_rules import TestReportBusinessRule

@receiver(post_save, sender=TestReport)
def execute_product_business_rules(sender, instance, **kwargs):
    TestReportBusinessRule.run_all(instance)