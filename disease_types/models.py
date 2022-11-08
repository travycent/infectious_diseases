from django.db import models

# Create your models here.
#Disease Type Model
class DiseaseTypesModel(models.Model):
    disease_type_id=models.AutoField(primary_key=True)
    disease_type_name=models.CharField(max_length=100)
    disease_type_desc=models.TextField(blank=True)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.disease_type_name
    class Meta:
        verbose_name_plural = 'Disease Types'
