from raptar.data_service.models.project import Project
from rest_framework import serializers
from raptar.data_service.serializers.product_serializer import ProductSerializer

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('projectname','projectowner','repositoryurl','product')
