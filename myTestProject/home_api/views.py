from django.shortcuts import render
from rest_framework import viewsets
from home_api.models import ProfileModels,CompanyModels,BlogModels,AuthorModels,EntryModels,EmpDetailsModels,EmpDesignationModels,CityModels
from home_api.serializers import ProfileSerializers,CompanySerializers,BlogSerializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response 
from django.db import connection
from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Count,Sum
################################################################
# Function Base API
################################################################
@api_view(['GET'])   
def get_single_blog(request, pk):
        try:            
            blog=BlogModels.objects.get(pk=pk)
            blog_data = {
            'id': blog.id,
            'name': blog.name,
            'tagline': blog.tagline,
            # Add more fields as needed
            }     
             
            return Response(blog_data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            }) 
        
@api_view(['GET'])          
def get_all_blog(request):
        try:            
            blog=BlogModels.objects.all()
            blog_data = list(blog.values())
            return Response(blog_data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })          
        
@api_view(['GET'])   
def update_blog(request, pk):
        try:
            print("------")
            print(pk) 
                 
            blog=BlogModels.objects.get(pk=pk)
            blog.name ='Update -Blog'        
            blog.save()
            return Response({
                'message':'Update Success'
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })         
        
@api_view(['POST'])   
def add_blog(request):
        try: 
            data = request.data                
            b = BlogModels(name=data["name"], tagline=data["tagline"])   
            b.save()         
            return Response({
                'message':'add success'
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            }) 
        
@api_view(['POST'])   
def add_designation(request):
        try: 
            data = request.data                
            b = EmpDesignationModels(desName=data["name"])   
            b.save()         
            return Response({
                'message':'add emp Designation success'
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })  
               
@api_view(['POST'])   
def add_Emp_Details(request):
        try: 
            data = request.data    
            company_instance = CompanyModels.objects.get(Comp_Id=data["comp_Id"], default=0)
            empDes_instance = EmpDesignationModels.objects.get(des_Id=data["des_Id"])     
            if company_instance == 0:
             company_instance = None       
            b = EmpDetailsModels(
               empName=data["name"],
               empAge=data["age"],
               empSalary=data["salary"],
               empShift=data["shift"],
               empHoby=data["empHoby"],
               ratings=data["ratings"],
               Comp_Id=company_instance,
               des_Id=empDes_instance
               )   
            b.save()         
            return Response({
                'message':'add emp Details success'
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })  

@api_view(['GET'])   
def get_Test_Queries(request, pk,seqNo):
        try:
            res_data=""
            if seqNo==1: # filter with single field
               model=BlogModels.objects.filter(tagline='123')  
               model_data = list(model.values()) 
               res_data = model_data

            if seqNo==2: # get all emp designation http://127.0.0.1:8000/api/v1/test/1/2/
               model=EmpDesignationModels.objects.all()  
               model_data = list(model.values()) 
               res_data = model_data 

            if seqNo==3: # get all emp details http://127.0.0.1:8000/api/v1/test/1/3/
               model=EmpDetailsModels.objects.all()  
               model_data = list(model.values()) 
               res_data = model_data  

            #Retrieving specific objects with filters
            if seqNo==4: # get all emp details http://127.0.0.1:8000/api/v1/test/1/3/
               #filters  multiple
               #model=EmpDetailsModels.objects.filter(empName="Om",empAge="32")  

               # Retrieve all blogs where the tagline contains "Bar"
               #model = EmpDetailsModels.objects.filter(empHoby__contains="play")

               #Retrieve blogs where either name is "Foo" or tagline contains "Bar"
               #model = EmpDetailsModels.objects.filter(empName="Om") | EmpDetailsModels.objects.filter(empHoby__contains="play")
               
               #order by Asc
               #model = EmpDetailsModels.objects.order_by('empName')
               #order by Dsc
               #model = EmpDetailsModels.objects.order_by('-empName')

               #cheking isnull
               #model = EmpDetailsModels.objects.filter(empHoby__isnull=False,empSalary__gt=40000).exclude(empHoby__exact='')
               
               #Filter by Using two Models
               #designationModel = EmpDesignationModels.objects.get(desName="Programmer") 
               #model = EmpDetailsModels.objects.filter(des_Id=designationModel)
                
               #Retrieve blogs with a title starting with a specific letter               
               #model = EmpDetailsModels.objects.filter(empName__istartswith='N')

               #Retrieve blogs with a title containing any word in a list of keywords               
               #model = EmpDetailsModels.objects.annotate(rating_count=Count('ratings')).order_by('-rating_count')
               
               #Retrieve blogs that have been tagged with any of the given tags
               #tag_names = ['Sham','Ram']
               #model= EmpDetailsModels.objects.filter(empName__in=tag_names)

               #LIMT
               #model= EmpDetailsModels.objects.all()[5:10]  #[:5]

               #A case-insensitive match
               #model=EmpDetailsModels.objects.get(empname__iexact="beatles blog")

               #More Than Two Orders
               model= EmpDetailsModels.objects.order_by('empSalary','-empAge','ratings')

               model_data = list(model.values()) 
               res_data = model_data     

            if seqNo==5: # get all emp details http://127.0.0.1:8000/api/v1/test/1/3/
               model=CityModels.objects.all()  
               model_data = list(model.values()) 
               res_data = model_data 

             ##############################################

             #select_related Joins more tables Operations
            if seqNo==6:
               model= EmpDetailsModels.objects.select_related('Comp_Id', 'des_Id').all()
               employee_data = []
               for employee in model:
                employee_data.append({
                'name': employee.empName,
                'company': employee.Comp_Id.name_field,
                'designation': employee.des_Id.desName, 
                'ratings': employee.ratings,
                })
               
               res_data = employee_data  

            #**********************************************************************
            if seqNo==7: #Joins multiple Tables and  joins with .exclude
               model= EmpDetailsModels.objects.select_related('Comp_Id', 'city','des_Id').exclude(city__cityName__isnull=False).exclude(Comp_Id__name_field__isnull=True)
               employee_data = []
               for employee in model:
                city_name = employee.city.cityName if employee.city else None
                employee_data.append({
                'name': employee.empName,
                'company': employee.Comp_Id.name_field,
                'designation': employee.des_Id.desName,
                'city': city_name, 
                'ratings': employee.ratings,
                })
               
               res_data = employee_data 
            

            #*******************************More Operations select_related***************************************
            if seqNo==8: # get all emp details http://127.0.0.1:8000/api/v1/test/1/8/
               model= EmpDetailsModels.objects.select_related('Comp_Id', 'city','des_Id').exclude(city__cityName__isnull=False).exclude(Comp_Id__name_field__isnull=True).order_by('ratings')
               employee_data = []
               for employee in model:
                city_name = employee.city.cityName if employee.city else None
                employee_data.append({
                'name': employee.empName,
                'company': employee.Comp_Id.name_field,
                'designation': employee.des_Id.desName,
                'city': city_name, 
                'ratings': employee.ratings,
                })
               
               res_data = employee_data 


            #  Group by ratings using iterating 
            if seqNo==9: #  http://127.0.0.1:8000/api/v1/test/1/9/
               model= EmpDetailsModels.objects.select_related('Comp_Id', 'city','des_Id').exclude(city__cityName__isnull=False).exclude(Comp_Id__name_field__isnull=True).order_by('ratings')
               
               employee_data = {}
               for employee in model:
                if employee.ratings in employee_data:
                 employee_data[employee.ratings]['salary'] += employee.empSalary
                else:
                    employee_data[employee.ratings] = {
                        'salary': employee.empSalary,
                        'ratings': employee.ratings
                    }

                # Convert dictionary to list of dictionaries
                employee_list = [data for data in employee_data.values()]               
               
               res_data = employee_list 

            #  Group by ratings using annotate =Group By
            if seqNo==10: #  http://127.0.0.1:8000/api/v1/test/1/10/
               model= EmpDetailsModels.objects.values('ratings','empAge').annotate(
                    total_salary=Sum('empSalary'),
                    total_ratings=Sum('ratings'),
                    count_age=Count('empAge')
                )
               
               employee_data = []
               for employee in model:
                    employee_data.append({
                        'ratings': employee['ratings'],
                        'total_salary': employee['total_salary'],
                        'total_ratings': employee['total_ratings'],
                        'count_age': employee['count_age']
                })

                # Convert dictionary to list of dictionaries                           
               
               res_data = employee_data   



            return Response(res_data)

        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })    

@api_view(['POST'])   
def post_Test_Queries(request, pk,seqNo):
        
        if seqNo==1: # update Employee Details
            try:
                selected_field=""
                data = request.data
                blog=EmpDetailsModels.objects.get(pk=pk)
                if data.get('empName'):
                      selected_field=data["empName"]
                      blog.empName = data["empName"]
                if data.get('empAge'):
                      selected_field=data["empAge"]
                      blog.empAge = data["empAge"] 
                if data.get('empSalary'):
                      selected_field=data["empSalary"]
                      blog.empSalary = data["empSalary"]
                if data.get('empShift'):
                      selected_field=data["empShift"]
                      blog.empShift = data["empShift"]
                if data.get('ratings'):
                      selected_field=data["ratings"]
                      blog.ratings = data["ratings"] 
                if data.get('city'):
                      city_instance = CityModels.objects.get(pk=data["city"]) 
                      selected_field=data["city"]
                      blog.city = city_instance             
                if data.get('empHoby'):
                      selected_field=data["empHoby"]
                      print(data.get('empHoby'))
                      blog.empHoby = data["empHoby"]                        
                       
                blog.save()
                return Response({
                    'message':'Update Success '+ selected_field
                })
            except Exception as e:
                print(e)
                return Response({
                    'message':'Error'
                }) 

        if seqNo==2: # add city Details 
            try:                 
                data = request.data
                blog=CityModels(cityName=data["cityName"])
                blog.save()
                return Response({
                    'message':'Save Success '+ data["cityName"]
                })
            except Exception as e:
                print(e)
                return Response({
                    'message':'Error'
                })             
                     

################################################################
# View Base API
################################################################
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

class BlogAuthorEntryViewSet(viewsets.ModelViewSet):
     queryset  = BlogModels.objects.all()
     
     @action(detail=False,methods=['get'])
     def getBlogData(self,request):
        try:                
            blog=BlogModels.objects.all()            
           # return Response(blog)
            blog_data = list(blog.values())
            return Response(blog_data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })  

     @action(detail=False,methods=['POST']) 
     def addBlogData(self,request):
        try:
            data = request.data                
            b = BlogModels(name=data["name"], tagline=data["tagline"])   
            b.save()         
            return Response({
                'message':'success'
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })   
        
     @action(detail=False,methods=['get']) 
     def singleBlogData(self,request,pk=None):
        try:
            print(pk)  
            blog=BlogModels.objects.get(pk=pk)              
            blog_data = list(blog.values())
            return Response(blog_data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Error'
            })   


        
        

 