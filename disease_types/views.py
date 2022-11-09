from django.shortcuts import render

from rest_framework import viewsets
from .serializers import DiseaseTypeSerializer,UpdateDiseaseTypeSerializer
from .models import DiseaseTypesModel #Import all the models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#Get all the Data of the DiseaseReportSerializer
class DiseaseTypeViewSet(viewsets.ModelViewSet):
    queryset = DiseaseTypesModel.objects.all().order_by('created_on')
    serializer_class = DiseaseTypeSerializer

#Class to Manage Diseases
class DiseaseTypeApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=UpdateDiseaseTypeSerializer(data=request.data)
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
        queryset = DiseaseTypesModel.objects.all().order_by('created_on')
        serializer_class = UpdateDiseaseTypeSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific 
class DiseaseTypeDetailApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = DiseaseTypesModel.objects.filter(disease_type_id=id)
            serializer_class = UpdateDiseaseTypeSerializer(queryset, many=True)
            
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
        queryset = DiseaseTypesModel.objects.filter(disease_type_id=id).first()
        serializer_class = UpdateDiseaseTypeSerializer(queryset, data=request.data)
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
