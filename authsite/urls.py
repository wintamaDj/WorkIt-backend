from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),
    # path('admin/', admin.site.urls),
]