from django.db import models
from raptar.data_service.models.project import Project


class Pipeline(models.Model):
    pipelineid = models.AutoField(primary_key=True)
    url = models.CharField(max_length=250)
    commitid = models.IntegerField(help_text='Github commit id')
    jobid = models.IntegerField(help_text='Jenkins Build Id')
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(null=True)
    duration =models.IntegerField(help_text='Time in Seconds',null=True)
    result =models.CharField(max_length=50,null=True)
    projectid = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self):
        return self.pipelineid