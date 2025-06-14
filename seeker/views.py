from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("[seeker api] Oops. Something went wrong, and you shouldn't be seeing this page! Please contact support or an admin")

# API views
from rest_framework import generics
from authsite.models import Seeker
from .serializers import *
# from rest_framework.permissions import IsAdminUser

class CreateUser_Seeker(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='SEEKER')
    serializer_class = UserSerializer

    def create(self, validated_data):
        return Seeker.objects.create(**validated_data)

# class Read_Profile(generics.ListAPIView):
#     pass

class Update_SeekerProfile(generics.RetrieveUpdateAPIView):
    queryset = seeker_profile.objects.all()
    serializer_class = SeekerProfileSerializer

class List_Company(generics.ListAPIView):
    queryset = User.objects.filter(role='COMPANY')
    serializer_class = ListUserSerializer

# add per view for perms:
# permission_classes = [*insert perm model*]