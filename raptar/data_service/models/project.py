from django.db import models
from raptar.data_service.models.product import Product


class Project(models.Model):
    projectid = models.AutoField(primary_key=True)
    projectname = models.CharField(max_length=250)
    projectowner = models.CharField(max_length=50)
    repositoryurl = models.CharField(max_length=250)
    environment = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.projectid