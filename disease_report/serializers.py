# serializers.py --This file will serialize all the data of this app
from rest_framework import serializers #import the serializer
from .models import DiseaseReportModel,view_hospital_d,TempUser,DiseaseReportGeneralSummary,DistrictDiseaseReportSummary,HospitalDiseaseReportSummary,HospitalBasedDiseaseReport #Import all the models in the APP
from django.db.models import Sum
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
# Get the Sums of all diseases
class GetSumDiseaseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempUser
        fields ='__all__'
# Get the Sums of all diseases
class DiseaseReportGeneralSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseReportGeneralSummary
        fields =('disease_type_id','discharge_count','new_case_count','death_count')
        disease_report_id_id = serializers.IntegerField()
# Get the Sums of all District Data
class DistrictDiseaseReportSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictDiseaseReportSummary
        fields =('disease_type_id','district_name','discharge_count','new_case_count','death_count','created_day')
        disease_report_id_id = serializers.IntegerField()
# Get the Sums of all District Data
class HospitalDiseaseReportSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalDiseaseReportSummary
        fields =('disease_type_id','hospital_name','discharge_count','new_case_count','death_count','created_day')
        disease_report_id_id = serializers.IntegerField()
class HospitalBasedDiseaseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalBasedDiseaseReport
        fields =('disease_type_id','location','district_name','hospital_name','discharge_count','new_case_count','death_count','created_day')
        