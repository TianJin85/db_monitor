from rest_framework import serializers

from .models import MonitoringLog, MonitoringConfig, MonitoringInfo, MonitoringRun


class MonitoringLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringLog
        fields = '__all__'


class MonitoringConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringConfig
        fields = '__all__'


class MonitoringInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringInfo
        fields = '__all__'


class MonitoringRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringRun
        fields = '__all__'
