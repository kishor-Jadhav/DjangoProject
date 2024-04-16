from django.contrib import admin
from django.urls import path,include
from home_api.views import ProfileViewSet,CompanyViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profile',ProfileViewSet,basename='profile')
router.register(r'company',CompanyViewSet,basename='company')
urlpatterns = [
    path('',include(router.urls)),
    
]