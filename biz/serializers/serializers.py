from rest_framework import serializers
from root.models import *
from biz.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ComapnyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = company_profile
        fields = [
            'id',
            'pic',
            'industry',
            'address',
            'contact',
        ]