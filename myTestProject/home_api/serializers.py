from rest_framework import serializers
from home_api.models import ProfileModels,CompanyModels
class ProfileSerializers(serializers.ModelSerializer):
   # profile_Id = serializers.ReadOnlyField()
    class Meta:
        model = ProfileModels
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
   # profile_Id = serializers.ReadOnlyField()
    class Meta:
        model = CompanyModels
        fields = '__all__'        
