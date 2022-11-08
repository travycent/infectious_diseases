# hospitals/urls.py
from django.conf.urls import url
from django.urls import path
from .views import DistrictApi,DistrictDetailApi,HospitalApi,HospitalDetailApi

#Add Our API URLS
urlpatterns = [
    path('districts/', DistrictApi.as_view(),name="Districts"),
    path('districts/<int:id>/', DistrictDetailApi.as_view(),name="Districts Detail"),
    path('hospitals/', HospitalApi.as_view(),name="Hospitals"),
    path('hospitals/<int:id>/', HospitalDetailApi.as_view(),name="Hospital Detail"),
    
]
