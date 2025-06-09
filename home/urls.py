from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('seeker/home/', List_Company.as_view(), name='User Home'),   
    path('seeker/register/', CreateUser_Seeker.as_view(), name='Register Seeker'),
    path('seeker/profile/<int:pk>/', Update_SeekerProfile.as_view(), name='Seeker Profile'),
    path('company/home/', index, name='placeholder'),
    path('company/register/', CreateUser_Company.as_view(), name='Register Company'),
    path('company/profile/<int:pk>/', Update_CompanyProfile.as_view(), name='Company Profile'),
]