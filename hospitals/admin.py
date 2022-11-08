from django.contrib import admin
# Register your models here.
from .models import DistrictModel,HospitalsModel
#Districts Display Admin
class DistrictsAdmin(admin.ModelAdmin):
    list_display= ('district_name','created_on',  )#Display Data in A List
    search_fields = ('district_id','created_on')#Add A search Field
#Hospitals Display Admin
class HospitalsAdmin(admin.ModelAdmin):
    list_display= ('hospital_name','district_id','assigned_number','created_on',  )#Display Data in A List
    search_fields = ('hospital_id','district_id','hospital_name','created_on')#Add A search Field
#Register Models
admin.site.register(DistrictModel,DistrictsAdmin)
admin.site.register(HospitalsModel,HospitalsAdmin)

