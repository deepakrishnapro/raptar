from django.db import models
from raptar.data_service.models.pipeline import Pipeline

class TestReport(models.Model):
    totaltestcase = models.IntegerField()
    testcasepassed = models.IntegerField()
    testcasefailed = models.IntegerField()
    testcaseskipped = models.IntegerField()
    passpercent =models.IntegerField()
    pipelineid = models.ForeignKey(Pipeline, on_delete=models.CASCADE)

    def __str__(self):
        return self.pipelineid