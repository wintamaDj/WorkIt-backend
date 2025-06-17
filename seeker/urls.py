from django.urls import path, include
from .views import *
from biz.views import List_Company

profile = [
    # path('profile/<int:pk>/edit/', Edit_SeekerProfile.as_view(), name='Modify Seeker Profile'), # DRF requires key in url
    # path('profile/<int:pk>/', View_SeekerProfile.as_view(), name='View Seeker Profile'),
    path('profile/<int:pk>/', ViewEdit_SeekerProfile.as_view(), name='View and Modify Seeker Profile'),
]

edu = [
    path('add/', Create_education_details.as_view(), name='Add educational experience'),
    path('<int:pk>/edit/', Edit_education_details.as_view(), name='Edit edu card'),
    path('<int:pk>/', View_education_details.as_view(), name='View edu card'),
]

career = [
    path('add/', Create_user_timeline_jobs.as_view, name='add new job experience'),
    path('<int:pk>/edit/', Edit_user_timeline_jobs.as_view(), name='Edit employment history'),
    path('<int:pk>/', View_user_timeline_jobs.as_view(), name='View seeker career history'),
]

# main router
urlpatterns = [
    # path('', index, name='index'),
    # path('main/', index, name='placeholder'),
    path('', List_Company.as_view(), name='Lists Companies'),   
    path('register/', Create_User_Seeker.as_view(), name='Register Seeker'),
    path('profile/', include(profile)),
    path('education/', include(edu)),
    path('career/', include(career)),
]