from rest_framework import serializers
from home_api.models import ProfileModels,CompanyModels,BlogModels,AuthorModels,EntryModels
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

class BlogSerializers(serializers.ModelSerializer):   
    class Meta:
        model = BlogModels
        fields = '__all__' 

class AuthorSerializers(serializers.ModelSerializer):   
    class Meta:
        model = AuthorModels
        fields = '__all__'

class EntrySerializers(serializers.ModelSerializer):   
    class Meta:
        model = EntryModels
        fields = '__all__'        
