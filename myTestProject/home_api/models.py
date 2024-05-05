from django.db import models
from datetime import date

# Create your models here.
class ProfileModels(models.Model):
    profile_Id = models.AutoField(primary_key=True)
    name_field = models.TextField()
    age_field = models.IntegerField()

class CompanyModels(models.Model):
    Comp_Id = models.AutoField(primary_key=True)
    name_field = models.TextField()
    year_field = models.IntegerField()
    profile_Id =models.ForeignKey(ProfileModels, on_delete=models.CASCADE)   

class BlogModels(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
    
class AuthorModels(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class EntryModels(models.Model):
    blog = models.ForeignKey(BlogModels, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(AuthorModels)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline   


class EmpDesignationModels(models.Model):
    des_Id = models.AutoField(primary_key=True)
    desName = models.TextField()   
    def __str__(self):
        return self.desName    
    
class CityModels(models.Model):
    city = models.AutoField(primary_key=True)
    cityName = models.TextField()   
    def __str__(self):
        return self.cityName      
 
               
class EmpDetailsModels(models.Model):
    Emp_Id = models.AutoField(primary_key=True)
    empName = models.TextField()
    empAge = models.IntegerField()
    empSalary = models.IntegerField()
    empShift = models.TextField()
    empHoby = models.TextField()
    ratings = models.IntegerField()
    Comp_Id =models.ForeignKey(CompanyModels, on_delete=models.SET_NULL,null=True,default=None)
    des_Id =models.ForeignKey(EmpDesignationModels, on_delete=models.CASCADE)  
    city = models.ForeignKey(CityModels, on_delete=models.SET_NULL,null=True, blank=True,default=None)
    def __str__(self):
        return self.empName

