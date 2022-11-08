from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
# Create your models here.
#Districts Model
class DistrictModel(models.Model):
    district_id=models.AutoField(primary_key=True)
    district_name=models.CharField(unique=True,max_length=100)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.district_name
    class Meta:
        verbose_name_plural = 'District Details'
#Hospitals Model
class HospitalsModel(models.Model):
    hospital_id=models.AutoField(primary_key=True)
    district_id=models.ForeignKey(DistrictModel,on_delete=models.CASCADE)
    hospital_name=models.CharField(max_length=100)
    assigned_number=models.IntegerField(unique=True)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hospital_name
    class Meta:
        verbose_name_plural = 'Hospitals Details'

