from django.db  import models


class TestSuite(models.Model):
    testsuiteid = models.AutoField(primary_key=True)
    testsuitename = models.CharField(max_length=255)
    owner = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.testsuiteid