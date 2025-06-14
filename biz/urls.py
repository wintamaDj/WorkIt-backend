from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('main/', index, name='placeholder'),
    path('register/', CreateUser_Company.as_view(), name='Register Company'),
    path('profile/<int:pk>/', Update_CompanyProfile.as_view(), name='Company Profile'),
]