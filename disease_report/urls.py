# mtnpulseapp/urls.py
from django.conf.urls import url
from django.urls import path
from .views import DiseaseReportApi,DiseaseReportDetailApi,TestApi,DiseaseReportGeneralSummaryApi,DistrictDiseaseReportSummaryApi,HospitalDiseaseReportSummaryApi,DiseaseTrendReportApi,HospitalBasedDiseaseReportApi


#Add Our API URLS
urlpatterns = [
    path('disease-reports/', DiseaseReportApi.as_view(),name="Disease Reports"),
    path('disease-reports/<int:id>/', DiseaseReportDetailApi.as_view(),name="Disease Reports Detail"),
    path('disease-test/', TestApi.as_view(),name="Summary Reports Detail"),
    path('general-disease-summary/<int:id>/<str:date_from>/<str:date_to>/', DiseaseReportGeneralSummaryApi.as_view(),name="General Disease Summary"),
    path('district-disease-summary/<int:id>/<str:district_id>/<str:date_from>/<str:date_to>/', DistrictDiseaseReportSummaryApi.as_view(),name="Districts Disease Summary"),
    path('hospital-disease-summary/<int:id>/<str:hospital_id>/<str:date_from>/<str:date_to>/', HospitalDiseaseReportSummaryApi.as_view(),name="Hospitals Disease Summary"),
    path('disease-trend-summary/<int:id>/<str:district_id>/<str:hospital_id>/<str:date_from>/<str:date_to>/', DiseaseTrendReportApi.as_view(),name="Disease Trend Summary"),
    path('sorted-disease-report-summary/<int:id>/<str:district_id>/<str:hospital_id>/<str:date_from>/<str:date_to>/', HospitalBasedDiseaseReportApi.as_view(),name="Sorted Disease Report Summary"),
    # disease_type_id,date_from,date_to district_id
    
]
