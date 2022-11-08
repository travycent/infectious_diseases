from django.contrib import admin

# Register your models here.
from .models import DiseaseTypesModel
#Register all Models
class DiseaseTypesAdmin(admin.ModelAdmin):
    list_display= ('disease_type_name','disease_type_desc',  'created_on')#Display Data in A List
    search_fields = ('disease_type_id','disease_type_name')#Add A search Field
#Register Models
admin.site.register(DiseaseTypesModel,DiseaseTypesAdmin)

