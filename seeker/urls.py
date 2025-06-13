from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('seeker/main/', List_Company.as_view(), name='User Home'),   
    path('seeker/register/', CreateUser_Seeker.as_view(), name='Register Seeker'),
    path('seeker/profile/<int:pk>/', Update_SeekerProfile.as_view(), name='Modify Seeker Profile'), # DRF requires key in url
    # path('seeker/jobList/', jobList.as_view(), name='Company Profile'),
    # path('auth/', include(rest_frameworks.urls, namespace='rest_framework')), # only for testing backend
    # path('auth/', include(),
]