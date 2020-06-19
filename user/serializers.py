from rest_framework import serializers
from .models import *



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        print("----------------serializers>UserListSerializer-----------------------")
        model = UserList
        fields = '__all__'
