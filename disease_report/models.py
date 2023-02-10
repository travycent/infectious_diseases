from unittest.util import _MAX_LENGTH
from django.db import models
from disease_types.models import DiseaseTypesModel
from hospitals.models import HospitalsModel
from django.db.models.deletion import CASCADE
from dbview.models import DbView

# Create your models here.
#Disease Report Model
class DiseaseReportModel(models.Model):
    disease_report_id=models.AutoField(primary_key=True)
    disease_type_id=models.ForeignKey(DiseaseTypesModel,on_delete=models.CASCADE)
    hospital_id=models.ForeignKey(HospitalsModel,on_delete=models.CASCADE)
    death_count=models.IntegerField(default=0)
    new_case_count=models.IntegerField(default=0)
    discharge_count=models.IntegerField(default=0)
    location=models.CharField(max_length=100,default='0,0')
    created_on= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Disease Reports'
class view_hospital_d(DbView):
    # ...
    disease_report_id=models.AutoField(primary_key=True)

    @classmethod
    def get_view_str(cls):
        return """
                    CREATE VIEW disease_report_view_hospital_d AS SELECT disease_report_id,hs.hospital_name,ds.district_name,ds.district_id,dr.disease_type_id_id  ,
                    SUM(death_count) AS death_count,SUM(new_case_count) AS new_case_count,
                    SUM(discharge_count) AS discharge_count, DATE(dr.created_on) AS created_day  
                    FROM disease_report_diseasereportmodel AS dr
                    LEFT JOIN hospitals_hospitalsmodel hs
                    ON 
                    dr.hospital_id_id =  hs. hospital_id
                    LEFT JOIN hospitals_districtmodel ds
                    ON 
                    hs.district_id_id =  ds. district_id
                    GROUP BY DATE(dr.created_on),dr.disease_type_id_id, hs.hospital_id
                    ;
            """
class TempUser(models.Model):
    disease_report_id=models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=255)
    district_name = models.CharField(max_length=255)
    district_id = models.IntegerField()
    disease_type_id_id = models.IntegerField()
    death_count = models.IntegerField()
    new_case_count = models.IntegerField()
    discharge_count = models.IntegerField()
    created_day = models.DateField()
    class Meta:
        managed = False
        db_table = "disease_report_view_hospital_d"
class DiseaseReportGeneralSummary(models.Model):
    disease_report_id=models.AutoField(primary_key=True)
    disease_type_id = models.IntegerField()
    death_count = models.IntegerField()
    new_case_count = models.IntegerField()
    discharge_count = models.IntegerField()
    created_day = models.DateField()
    class Meta:
        managed = False
        db_table = "view_disease_summary"
class DistrictDiseaseReportSummary(models.Model):
    disease_report_id=models.AutoField(primary_key=True)
    disease_type_id = models.IntegerField()
    district_name=models.CharField(max_length=255)
    district_id = models.IntegerField()
    death_count = models.IntegerField()
    new_case_count = models.IntegerField()
    discharge_count = models.IntegerField()
    created_day = models.DateField()
    class Meta:
        managed = False
        db_table = "view_districts_data"
class HospitalDiseaseReportSummary(models.Model):
    disease_report_id=models.AutoField(primary_key=True)
    disease_type_id = models.IntegerField()
    district_name=models.CharField(max_length=255)
    district_id = models.IntegerField()
    hospital_name=models.CharField(max_length=255)
    hospital_id = models.IntegerField()
    death_count = models.IntegerField()
    new_case_count = models.IntegerField()
    discharge_count = models.IntegerField()
    created_day = models.DateField()
    class Meta:
        managed = False
        db_table = "view_hospital_data"
class HospitalBasedDiseaseReport(models.Model):
    disease_report_id=models.AutoField(primary_key=True)
    disease_type_id = models.IntegerField()
    location=models.CharField(max_length=255)
    district_name=models.CharField(max_length=255)
    district_id = models.IntegerField()
    hospital_name=models.CharField(max_length=255)
    hospital_id = models.IntegerField()
    death_count = models.IntegerField()
    new_case_count = models.IntegerField()
    discharge_count = models.IntegerField()
    created_day = models.DateField()
    class Meta:
        managed = False
        db_table = "view_general_disease_report"
