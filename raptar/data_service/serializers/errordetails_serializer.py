from raptar.data_service.models.errordetails import ErrorDetails
from rest_framework import serializers


class ErrorDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ErrorDetails
        fields = '__all__'
