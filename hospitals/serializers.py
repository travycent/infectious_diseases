# serializers.py --This file will serialize all the data of this app
from rest_framework import serializers #import the serializer
from .models import DistrictModel,HospitalsModel #Import all the models in the APP

#DistrictSerializer for Create, Get,Delete
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictModel
        fields = ('district_id', 'district_name','created_on')
        district_id = serializers.IntegerField()
        district_name = serializers.CharField(max_length=100)
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance

#DistrictModel Serializers for Create, Get,Delete
class UpdateDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictModel
        fields = ('district_id', 'district_name','created_on')
        district_id = serializers.IntegerField()
        district_name = serializers.CharField(max_length=100)
        
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalsModel
        fields = ('district_id','hospital_id', 'hospital_name','assigned_number','created_on')
        district_id = serializers.IntegerField()
        hospital_id = serializers.IntegerField()
        hospital_name = serializers.CharField(max_length=100)
        assigned_number = serializers.IntegerField()
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance

#FilesModel Serializers for Create, Get,Delete
class UpdateHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalsModel
        fields = ('district_id','hospital_id', 'hospital_name','assigned_number','created_on')
        district_id = serializers.IntegerField()
        hospital_id = serializers.IntegerField()
        hospital_name = serializers.CharField(max_length=100)
        assigned_number = serializers.IntegerField()