from rest_framework import serializers
from .models import *


class AppListSerializer( serializers.ModelSerializer ):
    class Meta:
        print("----------------serializers>UserListSerializer-----------------------")
        model = AppList
        fields = '__all__'
