from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("[seeker api] Oops. Something went wrong, and you shouldn't be seeing this page! Please contact support or an admin")

# API views
from rest_framework import generics
from authsite.models import Seeker
from .serializers import *
# from rest_framework.permissions import IsAdminUser

# add per view for perms:
# permission_classes = [*insert perm model*]

# Create your views below

# User
class Create_User_Seeker(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='SEEKER')
    serializer_class = UserSerializer
    # permission_classes = [DjangoModelPermissions]

    def create(self, validated_data):
        return Seeker.objects.create(**validated_data)

# Profile
class Edit_SeekerProfile(generics.RetrieveUpdateAPIView):
    queryset = seeker_profile.objects.all()
    serializer_class = SeekerProfileSerializer
    # permission_classes = [DjangoModelPermissions]

class View_SeekerProfile(generics.ListAPIView):
    queryset = seeker_profile.objects.all()
    serializer_class = SeekerProfileSerializer
    # permission_classes = [DjangoModelPermissions]

# education_details
class Create_education_details(generics.CreateAPIView):
    queryset = education_details.objects.all()
    # serializer_class = education_details_serializer
    # permission_classes = [DjangoModelPermissions]

class Edit_education_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = education_details.objects.all()
    # serializer_class = education_details_serializer
    # permission_classes = [DjangoModelPermissions]

class View_education_details(generics.ListAPIView):
    queryset = education_details.objects.all()
    # serializer_class = education_details_serializer
    # permission_classes = [DjangoModelPermissions]

# timeline_jobs
class Create_user_timeline_jobs(generics.CreateAPIView):
    queryset = user_timeline_jobs.objects.all()
    # serializer_class = user_timeline_jobs_serializer
    # permission_classes = [DjangoModelPermissions]

class Edit_user_timeline_jobs(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_timeline_jobs.objects.all()
    # serializer_class = user_timeline_jobs_serializer
    # permission_classes = [DjangoModelPermissions]

class View_user_timeline_jobs(generics.ListAPIView):
    queryset = user_timeline_jobs.objects.all()
    # serializer_class = user_timeline_jobs_serializer
    # permission_classes = [DjangoModelPermissions]

# review
class Edit_user_reviews(generics.RetrieveUpdateAPIView):
    queryset = user_reviews.objects.all()
    # serializer_class = user_reviews_serializer
    # permission_classes = [DjangoModelPermissions]

class View_user_reviews(generics.ListAPIView):
    queryset = user_reviews.objects.all()
    # serializer_class = user_reviews_serializer
    # permission_classes = [DjangoModelPermissions]