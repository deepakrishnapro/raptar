from raptar.data_service.models.pipeline import Pipeline
from rest_framework import serializers

class PipelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pipeline
        fields = '__all__'
