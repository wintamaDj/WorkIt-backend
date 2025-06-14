from django.shortcuts import render
from django.http import HttpResponse

# Placeholder view
def index(request):
    return HttpResponse("[biz api] Oops. Something went wrong, and you shouldn't be seeing this page! Please contact support or an admin")

# API views
from rest_framework import generics
from authsite.models import User, Company
from .serializers import *
from .models import *
# from rest_framework.permissions import IsAdminUser

# User and profile
class CreateUser_Company(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='COMPANY')
    serializer_class = UserSerializer

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    
class Update_CompanyProfile(generics.RetrieveUpdateAPIView):
    queryset = company_profile.objects.all()
    serializer_class = ComapnyProfileSerializer

# class Archive_Company(UpdateAPIView):
#     # set to not_active? 
#     pass