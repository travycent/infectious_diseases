# mtnpulseapp/urls.py
from django.conf.urls import url
from django.urls import path
from .views import DiseaseReportApi,DiseaseReportDetailApi

#Add Our API URLS
urlpatterns = [
    path('disease-reports/', DiseaseReportApi.as_view(),name="Disease Reports"),
    path('disease-reports/<int:id>/', DiseaseReportDetailApi.as_view(),name="Disease Reports Detail"),
    
]
