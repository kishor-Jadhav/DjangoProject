from django.contrib import admin
from django.urls import path,include
from home_api.views import ProfileViewSet,CompanyViewSet,BlogAuthorEntryViewSet
from home_api.views import *
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profile',ProfileViewSet,basename='profile')
router.register(r'company',CompanyViewSet,basename='company')
router.register(r'complex',BlogAuthorEntryViewSet,basename='complex')
urlpatterns = [
    path('',include(router.urls)),
    path('blog/<int:pk>/', get_single_blog, name='get_blog'),
    path('blog/', get_all_blog, name='get_blog'),
    path('blog/update/<int:pk>/', update_blog, name='get_blog'),
    path('blog/add/', add_blog, name='add_blog'),
    path('emp/adddes/', add_designation, name='add_designation'),
    path('emp/', add_Emp_Details, name='add_Emp_Details'),
    path('test/<int:pk>/<int:seqNo>/', get_Test_Queries, name='get_Test_Queries'),
    path('testadd/<int:pk>/<int:seqNo>/', post_Test_Queries, name='post_Test_Queries'),
]