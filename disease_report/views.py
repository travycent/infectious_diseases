from django.shortcuts import render

from rest_framework import viewsets
from .serializers import DiseaseReportSerializer,UpdateDiseaseReportSerializer,GetSumDiseaseReportSerializer,DiseaseReportGeneralSummarySerializer,DistrictDiseaseReportSummarySerializer,HospitalDiseaseReportSummarySerializer,HospitalBasedDiseaseReportSerializer
#Import all the models
from .models import DiseaseReportModel,view_hospital_d,TempUser,DiseaseReportGeneralSummary,DistrictDiseaseReportSummary,HospitalDiseaseReportSummary,HospitalBasedDiseaseReport
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Sum

#Get all the Data of the DiseaseReportSerializer
class DiseaseReportViewSet(viewsets.ModelViewSet):
    queryset = DiseaseReportModel.objects.all().order_by('created_on')
    serializer_class = DiseaseReportSerializer

#Class to Manage Diseases
class DiseaseReportApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=UpdateDiseaseReportSerializer(data=request.data)
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
        queryset = DiseaseReportModel.objects.all().order_by('created_on')
        serializer_class = DiseaseReportSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific 
class DiseaseReportDetailApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = DiseaseReportModel.objects.filter(disease_report_id=id)
            serializer_class = UpdateDiseaseReportSerializer(queryset, many=True)
            
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
        queryset = DiseaseReportModel.objects.filter(disease_report_id=id).first()
        serializer_class = UpdateDiseaseReportSerializer(queryset, data=request.data)
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
    
class TestApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request):
        queryset = TempUser.objects.all().values()
        serializer_class = GetSumDiseaseReportSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)

class DiseaseReportGeneralSummaryApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id,date_from,date_to=""):
            response_array={}
            if date_to != "null":
                queryset = DiseaseReportGeneralSummary.objects.filter(disease_type_id=id,created_day__range=[date_from,date_to])
                q1 = queryset.values("disease_type_id").annotate(death_count=Sum("death_count"), new_case_count=Sum("new_case_count"), discharge_count=Sum("discharge_count"), )
                serializer_class = DiseaseReportGeneralSummarySerializer(q1, many=True)
                
                if  len(serializer_class.data) > 0:
                    response_array=serializer_class.data[0]
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            else:
                queryset = DiseaseReportGeneralSummary.objects.filter(disease_type_id=id,created_day=date_from)
                serializer_class = DiseaseReportGeneralSummarySerializer(queryset, many=True)
                
                if  len(serializer_class.data) > 0:
                    response_array=serializer_class.data[0]
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
class DistrictDiseaseReportSummaryApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id,district_id,date_from,date_to=""):
            response_array={}
            if district_id != "null" and date_to != "null":
                queryset = DistrictDiseaseReportSummary.objects.filter(disease_type_id=id,district_id=district_id,created_day__range=[date_from,date_to])
                q1 = queryset.values("disease_type_id","district_id","district_name").annotate(death_count=Sum("death_count"), new_case_count=Sum("new_case_count"), discharge_count=Sum("discharge_count"), )
                serializer_class = DistrictDiseaseReportSummarySerializer(q1, many=True)
                
                if  len(serializer_class.data) > 0:
                    response_array=serializer_class.data[0]
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif district_id == "null" and date_to != "null":
                queryset = DistrictDiseaseReportSummary.objects.filter(disease_type_id=id,created_day__range=[date_from,date_to])
                q1 = queryset.values("disease_type_id","district_name").annotate(death_count=Sum("death_count"), new_case_count=Sum("new_case_count"), discharge_count=Sum("discharge_count"), )
                serializer_class = DistrictDiseaseReportSummarySerializer(q1, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif district_id == "null" and date_to == "null":
                queryset = DistrictDiseaseReportSummary.objects.filter(disease_type_id=id,created_day=date_from)
                serializer_class = DistrictDiseaseReportSummarySerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif district_id != "null" and date_to == "null":
                queryset = DistrictDiseaseReportSummary.objects.filter(disease_type_id=id,district_id=district_id,created_day=date_from)
                serializer_class = DistrictDiseaseReportSummarySerializer(queryset, many=True)
                
                if  len(serializer_class.data) > 0:
                    response_array=serializer_class.data[0]
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
class HospitalDiseaseReportSummaryApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id,hospital_id,date_from,date_to=""):
            response_array={}
            if hospital_id != "null" and date_to != "null":
                queryset = HospitalDiseaseReportSummary.objects.filter(disease_type_id=id,hospital_id=hospital_id,created_day__range=[date_from,date_to])
                q1 = queryset.values("disease_type_id","hospital_id","hospital_name").annotate(death_count=Sum("death_count"), new_case_count=Sum("new_case_count"), discharge_count=Sum("discharge_count"), )
                serializer_class = HospitalDiseaseReportSummarySerializer(q1, many=True)
                
                if  len(serializer_class.data) > 0:
                    response_array=serializer_class.data[0]
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif hospital_id == "null" and date_to != "null":
                queryset = HospitalDiseaseReportSummary.objects.filter(disease_type_id=id,created_day__range=[date_from,date_to])
                q1 = queryset.values("disease_type_id","hospital_id","hospital_name").annotate(death_count=Sum("death_count"), new_case_count=Sum("new_case_count"), discharge_count=Sum("discharge_count"), )
                serializer_class = HospitalDiseaseReportSummarySerializer(q1, many=True)
                
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif hospital_id == "null" and date_to == "null":
                queryset = HospitalDiseaseReportSummary.objects.filter(disease_type_id=id,created_day=date_from)
                serializer_class = HospitalDiseaseReportSummarySerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif hospital_id != "null" and date_to == "null":
                queryset = HospitalDiseaseReportSummary.objects.filter(disease_type_id=id,hospital_id=hospital_id,created_day=date_from)
                serializer_class = HospitalDiseaseReportSummarySerializer(queryset, many=True)
                
                if  len(serializer_class.data) > 0:
                    response_array=serializer_class.data[0]
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
class DiseaseTrendReportApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id,district_id,hospital_id,date_from,date_to=""):
            response_array={}
            if  district_id == "null" and hospital_id =="null" and date_to != "null":
                queryset = DiseaseReportGeneralSummary.objects.filter(disease_type_id=id,created_day__range=[date_from,date_to])
                serializer_class = DiseaseReportGeneralSummarySerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif  district_id != "null" and hospital_id =="null" and date_to != "null":
                queryset = DistrictDiseaseReportSummary.objects.filter(disease_type_id=id,district_id=district_id,created_day__range=[date_from,date_to])
                serializer_class = DistrictDiseaseReportSummarySerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif  district_id == "null" and hospital_id !="null" and date_to != "null":
                queryset = HospitalDiseaseReportSummary.objects.filter(disease_type_id=id,hospital_id=hospital_id,created_day__range=[date_from,date_to])
                serializer_class = HospitalDiseaseReportSummarySerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            else:
                queryset = DiseaseReportGeneralSummary.objects.filter(disease_type_id=id,created_day=date_from)
                serializer_class = DiseaseReportGeneralSummarySerializer(queryset, many=True)
                
                if  len(serializer_class.data) > 0:
                    response_array=serializer_class.data[0]
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
class HospitalBasedDiseaseReportApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id,district_id,hospital_id,date_from,date_to=""):
            response_array={}
            if  district_id == "null" and hospital_id =="null" and date_to != "null":
                queryset = HospitalBasedDiseaseReport.objects.filter(disease_type_id=id,created_day__range=[date_from,date_to])
                serializer_class = HospitalBasedDiseaseReportSerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif  district_id != "null" and hospital_id =="null" and date_to != "null":
                queryset = HospitalBasedDiseaseReport.objects.filter(disease_type_id=id,district_id=district_id,created_day__range=[date_from,date_to])
                serializer_class = HospitalBasedDiseaseReportSerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
            elif  district_id == "null" and hospital_id !="null" and date_to != "null":
                queryset = HospitalBasedDiseaseReport.objects.filter(disease_type_id=id,hospital_id=hospital_id,created_day__range=[date_from,date_to])
                serializer_class = HospitalBasedDiseaseReportSerializer(queryset, many=True)
                response_array=serializer_class.data
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': response_array,
                }
                return Response(response,status=status_code)
