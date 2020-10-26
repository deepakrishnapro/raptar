from django.contrib import admin
from raptar.data_service.models.project import Project
from raptar.data_service.models.product import Product

# Register your models here.

admin.site.register(Project)
admin.site.register(Product)