from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC
from business_rules.variables import BaseVariables, numeric_rule_variable, \
    string_rule_variable, select_rule_variable
from django.utils import timezone
from django_business_rules.business_rule import BusinessRule

from raptar.data_service.models.product import Product

class ProductVariables(BaseVariables):

    def __init__(self, product):
        self.product = product

    @numeric_rule_variable
    def product_version(self):
        return self.product.productversion


class ProductActions(BaseActions):

    def __init__(self, product):
        self.product = product

    @rule_action(params={"new_version": FIELD_NUMERIC})
    def put_on_sale(self, new_version):
        self.product.productversion = new_version
        self.product.save()

class ProductBusinessRule(BusinessRule):
    name = 'Product rules'
    variables = ProductVariables
    actions = ProductActions