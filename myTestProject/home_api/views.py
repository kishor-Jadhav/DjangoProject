from django.shortcuts import render
from rest_framework import viewsets
from home_api.models import ProfileModels,CompanyModels
from home_api.serializers import ProfileSerializers,CompanySerializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import connection

 
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset  = ProfileModels.objects.all()
    serializer_class = ProfileSerializers

    #api/v1/profile/1/getCompaniesById
    @action(detail=True,methods=['get'])
    def getCompaniesById(self,request,pk=None):
        try:                
            profileId=ProfileModels.objects.get(pk=pk)
            comp=CompanyModels.objects.filter(profile_Id=profileId)
            comp_serializer=CompanySerializers(comp,many=True,context={'request':request})
            return Response(comp_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Profile might not exists !! Error'
            })

    @action(detail=True,methods=['get'])
    def getCompaniesByIdBySQL(self,request,pk=None):
        try:                
            query ="SELECT * FROM home_api_companymodels inner join home_api_profilemodels on home_api_companymodels.profile_Id_id=home_api_profilemodels.profile_Id "
            # Execute the SQL query
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()  # Fetch all rows returned by the query

            results = []
            for row in rows:
                result_dict = {}
                result_dict['comp_Id'] = row[0]  # Assuming id is the first column
                result_dict['comp_name'] = row[1]  # Assuming name is the second column
                result_dict['year'] = row[2]  # Assuming industry is the third column
                result_dict['profile_name'] = row[5]  # Assuming headquarters is the fourth column
                result_dict['age'] = row[6]  # Assuming founded_year is the fifth column
                results.append(result_dict)
            # Process the query result as needed
            # Here, you might serialize the data or perform any other operations
            return Response(results)
        except Exception as e:
            print(e)
            return Response({
                'message':'Profile might not exists !! Error'
            })    


class CompanyViewSet(viewsets.ModelViewSet):
    queryset  = CompanyModels.objects.all()
    serializer_class = CompanySerializers
   
    
        

 