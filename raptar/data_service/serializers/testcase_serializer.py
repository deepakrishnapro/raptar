from raptar.data_service.models.testcase import TestCase
from rest_framework import serializers


class TestCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCase
        fields = '__all__'
