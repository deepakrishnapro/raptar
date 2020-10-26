from raptar.data_service.models.testreport import TestReport
from rest_framework import serializers


class TestReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestReport
        fields = '__all__'
