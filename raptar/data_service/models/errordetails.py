from django.db import models
from raptar.data_service.models.testcase import TestCase

class ErrorDetails(models.Model):
    errormessage = models.CharField(max_length=250,null=True)
    errorstatus =models.CharField(max_length=50,null=True)
    testid = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    def __str__(self):
        return self.testid