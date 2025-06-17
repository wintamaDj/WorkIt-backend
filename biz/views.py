from django.shortcuts import render
from django.http import HttpResponse

# Placeholder view
def index(request):
    return HttpResponse("[biz api] Oops. Something went wrong, and you shouldn't be seeing this page! Please contact support or an admin")

# API views
from rest_framework import generics
from rest_framework.permissions import *
from authsite.models import User, Company
from .serializers import *
from .models import *

# User and profile
class Create_User_Company(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='COMPANY')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, validated_data):
        return Company.objects.create_user(**validated_data)
    
class Update_CompanyProfile(generics.RetrieveUpdateAPIView):
    queryset = company_profile.objects.all()
    serializer_class = ComapnyProfileSerializer
    # permission_classes = [DjangoModelPermissions]

class View_CompanyProfile(generics.RetrieveAPIView):
    queryset = company_profile.objects.all()
    serializer_class = ComapnyProfileSerializer
    permission_classes = [IsAuthenticated]

class List_Company(generics.ListAPIView):
    queryset = User.objects.filter(role='COMPANY')
    # serializer_class = ListCompanySerializer
    # permission_classes = [DjangoModelPermissions]

# class Archive_Company(UpdateAPIView):
#     # set to not_active? 
#     pass

# jobs
class Create_company_jobs(generics.CreateAPIView):
    queryset = company_jobs.objects.all()
    # serializer_class = company_jobs_serializer
    # permission_classes = [DjangoModelPermissions]

class Edit_company_jobs(generics.RetrieveUpdateDestroyAPIView):
    queryset = company_jobs.objects.all()
    # serializer_class = company_jobs_serializer
    # permission_classes = [DjangoModelPermissions]

class View_company_jobs(generics.ListAPIView):
    queryset = company_jobs.objects.all()
    # serializer_class = company_jobs_serializer
    # permission_classes = [DjangoModelPermissions]

# apply
class Create_job_applications(generics.CreateAPIView):
    queryset = job_applications.objects.all()
    # serializer_class = job_applications_serializer
    # permission_classes = [DjangoModelPermissions]

    #please edit for different sides
class Edit_job_applications(generics.RetrieveUpdateAPIView):
    queryset = job_applications.objects.all()
    # serializer_class = job_applications_serializer
    # permission_classes = [DjangoModelPermissions]

class Delete_job_applications(generics.DestroyAPIView):
    queryset = job_applications.objects.all()
    # serializer_class = job_applications_serializer
    # permission_classes = [DjangoModelPermissions]