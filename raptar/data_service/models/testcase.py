from django.db  import models
from raptar.data_service.models.pipeline import Pipeline
from raptar.data_service.models.testsuite import TestSuite

class TestCase(models.Model):
    testid = models.AutoField(primary_key=True)
    starttime = models.DateTimeField()
    testcasename = models.CharField(max_length=255)
    duration = models.IntegerField(help_text='Time in Seconds',null=True)
    result = models.CharField(max_length=50,null=True)
    pipelineid = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    testsuiteid = models.ForeignKey(TestSuite, on_delete=models.CASCADE)

    def __str__(self):
        return self.testid