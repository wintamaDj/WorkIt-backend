from django.contrib import admin
from django.urls import path, include
from .views import *
from seeker.views import Edit_user_reviews, View_user_reviews

profile = [
    path('<int:pk>/', View_CompanyProfile.as_view(), name='View Company Profile'),
    path('<int:pk>/edit/', Update_CompanyProfile.as_view(), name='Edit Company Profile'),
]

jobs = [
    path('', View_company_jobs.as_view(), name='View open positions'),
    path('edit/', Edit_company_jobs.as_view(), name='Edit company positions'),
    path('apply/', Create_job_applications.as_view(), name='seeker applies for this job'),
    path('applicants/<int:pk>/manage/', Edit_job_applications.as_view(), name='manage applicants for this job'),  # only accept/reject
    path('review/', View_user_reviews.as_view(), name='List reviews for this position'),
    path('review/<int:pk>/edit/', Edit_user_reviews.as_view(), name="User edits this job's review"),
]

urlpatterns = [
    path('', index, name='index'),
    # path('main/', index, name='placeholder'),
    path('register/', Create_User_Company.as_view(), name='Register Company'),
    path('profile/', include(profile)),
    path('jobList/', List_Company.as_view(), name='Company Profile'),
    path('jobs/create/', Create_company_jobs.as_view(), name='Create positions'),
    path('jobs/<int:pk>/', include(jobs)),
]