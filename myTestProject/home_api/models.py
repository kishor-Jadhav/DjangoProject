from django.db import models

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