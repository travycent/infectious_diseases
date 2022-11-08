# serializers.py --This file will serialize all the data of this app
from rest_framework import serializers #import the serializer
from .models import DiseaseTypesModel #Import all the models in the APP
#FileCategorySerializers for Create, Get,Delete
class DiseaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseTypesModel
        fields = ('disease_type_id', 'disease_type_name','disease_type_desc','created_on')
        disease_type_id = serializers.IntegerField()
        disease_type_name = serializers.IntegerField()
        disease_type_desc = serializers.CharField()
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance

#FilesModel Serializers for Create, Get,Delete
class UpdateDiseaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseTypesModel
        fields = ('disease_type_id', 'disease_type_name','disease_type_desc','created_on')
        disease_type_id = serializers.IntegerField()
        disease_type_name = serializers.IntegerField()
        disease_type_desc = serializers.CharField()