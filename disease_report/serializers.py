# serializers.py --This file will serialize all the data of this app
from rest_framework import serializers #import the serializer
from .models import DiseaseReportModel #Import all the models in the APP
#FileCategorySerializers for Create, Get,Delete
class DiseaseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseReportModel
        fields = ('disease_report_id', 'disease_type_id','hospital_id','death_count','new_case_count','discharge_count','location','created_on')
        disease_type_id = serializers.IntegerField()
        hospital_id = serializers.IntegerField()
        death_count = serializers.IntegerField()
        new_case_count = serializers.IntegerField()
        discharge_count = serializers.IntegerField()
        location = serializers.CharField(max_length=100)
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance

#FilesModel Serializers for Create, Get,Delete
class UpdateDiseaseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseReportModel
        fields = ('disease_report_id', 'disease_type_id','hospital_id','death_count','new_case_count','discharge_count','location','created_on')
        disease_type_id = serializers.IntegerField()
        hospital_id = serializers.IntegerField()
        death_count = serializers.IntegerField()
        new_case_count = serializers.IntegerField()
        discharge_count = serializers.IntegerField()
        location = serializers.CharField(max_length=100)