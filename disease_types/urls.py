# diseasetype/urls.py
from django.conf.urls import url
from django.urls import path
from .views import DiseaseTypeApi,DiseaseTypeDetailApi

#Add Our API URLS
urlpatterns = [
    path('disease-types/', DiseaseTypeApi.as_view(),name="Disease Types"),
    path('disease-types/<int:id>/', DiseaseTypeDetailApi.as_view(),name="Disease Types Detail"),
    
]
