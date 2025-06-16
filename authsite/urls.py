from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),
    # path('admin/', admin.site.urls),
    # path('auth/', include(rest_frameworks.urls, namespace='rest_framework')), # only for testing backend
]