from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("[API TEST] Oops. Something went wrong, and you shouldn't be seeing this page! Please contact support or an admin")

# api views
from rest_framework import generics
from .models.base_user import Seeker, Company
from .serializers.userProfiles import *
# from rest_framework.permissions import 

class CreateUser_Seeker(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='SEEKER')
    serializer_class = UserSerializer

    def create(self, validated_data):
        return Seeker.objects.create(**validated_data)
    pass

class CreateUser_Company(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='COMPANY')
    serializer_class = UserSerializer

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    pass

# class Read_Profile(generics.ListAPIView):
#     pass

class Update_SeekerProfile(generics.RetrieveUpdateAPIView):
    queryset = seeker_profile.objects.all()
    serializer_class = SeekerProfileSerializer

class Update_CompanyProfile(generics.RetrieveUpdateAPIView):
    queryset = company_profile.objects.all()
    serializer_class = ComapnyProfileSerializer

class List_Company(generics.ListAPIView):
    queryset = User.objects.filter(role='COMPANY')
    serializer_class = ListUserSerializer
    pass