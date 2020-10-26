from django.db import models


class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=250)
    productversion = models.CharField(max_length=10)

    def __str__(self):
        return self.productid
