from raptar.data_service.models.testsuite import TestSuite
from rest_framework import serializers


class TestSuiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestSuite
        fields = '__all__'
