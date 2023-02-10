from django.contrib import admin
# Register your models here.
from .models import DiseaseReportModel,view_hospital_d,TempUser
#Disease Report Display Admin
class DiseaseReportAdmin(admin.ModelAdmin):
    list_display= ('location','disease_type_id','hospital_id','death_count','new_case_count','discharge_count','created_on')#Display Data in A List
    search_fields = ('disease_report_id','location','disease_type_id','hospital_id','death_count','new_case_count','discharge_count','created_on')#Add A search Field
class Hospital(admin.ModelAdmin):
     list_display= ('disease_report_id','hospital_name')#Display Data in A List
    

#Register Models
admin.site.register(DiseaseReportModel,DiseaseReportAdmin)
admin.site.register(TempUser,Hospital)

