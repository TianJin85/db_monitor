from rest_framework import serializers

from .models import *


class RoleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoleList
        fields = '__all__'
