from unittest.util import _MAX_LENGTH
from django.db import models
from disease_types.models import DiseaseTypesModel
from hospitals.models import HospitalsModel
from django.db.models.deletion import CASCADE

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

