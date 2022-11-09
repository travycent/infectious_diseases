from django.shortcuts import render

from rest_framework import viewsets
from .serializers import DistrictSerializer,UpdateDistrictSerializer,HospitalSerializer,UpdateHospitalSerializer
from .models import DistrictModel,HospitalsModel #Import all the models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#Get all the Data of the Districts
class DistrictViewSet(viewsets.ModelViewSet):
    queryset = DistrictModel.objects.all().order_by('created_on')
    serializer_class = DistrictSerializer

#Class to Manage Districts
class DistrictApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=UpdateDistrictSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = DistrictModel.objects.all().order_by('created_on')
        serializer_class = DistrictSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific 
class DistrictDetailApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = DistrictModel.objects.filter(district_id=id)
            serializer_class = UpdateDistrictSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status_code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status_code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = DistrictModel.objects.filter(district_id=id).first()
        serializer_class = UpdateDistrictSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
#Get all the Data of the Hospitals
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = HospitalsModel.objects.all().order_by('created_on')
    serializer_class = HospitalSerializer

#Class to Manage Hospitals
class HospitalApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=UpdateHospitalSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = HospitalsModel.objects.all().order_by('created_on')
        serializer_class = HospitalSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific 
class HospitalDetailApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = HospitalsModel.objects.filter(hospital_id=id)
            serializer_class = UpdateHospitalSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status_code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status_code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = HospitalsModel.objects.filter(hospital_id=id).first()
        serializer_class = UpdateHospitalSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

