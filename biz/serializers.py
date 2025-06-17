from rest_framework import serializers
from authsite.models import *
from biz.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # def validate_this(self, value):
    #     if value <=0:
    #         raise serializers.ValidationError(
    #             "price must be greathar than 0"
    #         )

class RegisterCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [

        ]

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