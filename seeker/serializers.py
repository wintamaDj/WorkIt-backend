# from django.contrib.auth.models import Group, User
# from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

from rest_framework import serializers
from authsite.models import *
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class SeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = seeker_profile
        fields = [
            'id',
            'pic',
            'resume',
        ]

# serializer method averages user review

# how to implement ser. methods:
# class UserSerializer(serializers.ModelSerializer):
#     days_since_joined = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = '__all__'

#     def get_days_since_joined(self, obj):
#         return (now() - obj.date_joined).days