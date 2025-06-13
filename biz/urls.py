from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('company/main/', index, name='placeholder'),
    path('company/register/', CreateUser_Company.as_view(), name='Register Company'),
    path('company/profile/<int:pk>/', Update_CompanyProfile.as_view(), name='Company Profile'),
]