from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions

from .serializers import *


class ApiMonitoringLog(generics.ListAPIView):
    queryset = MonitoringLog.objects.all().order_by('-log_time')
    serializer_class = MonitoringLogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['tags', 'log_level']
    search_fields = ['log_content']
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMonitoringConfig(generics.ListCreateAPIView):
    queryset = MonitoringConfig.objects.get_queryset().order_by('-type')
    serializer_class = MonitoringConfigSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('type', 'name',)
    search_fields = ('type', 'name',)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMonitoringConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitoringConfig.objects.get_queryset().order_by('id')
    serializer_class = MonitoringConfigSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMonitoringInfo(generics.ListCreateAPIView):
    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        if tags:
            return MonitoringInfo.objects.filter(tags=tags).order_by('id')
        else:
            return MonitoringInfo.objects.all()

    serializer_class = MonitoringInfoSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMonitoringInfoHis(generics.ListCreateAPIView):
    queryset = MonitoringInfo.objects.get_queryset().order_by('-id')
    serializer_class = MonitoringInfoSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags',)
    search_fields = ('tags', 'alarm_content',)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMonitoringRun(generics.ListCreateAPIView):
    queryset = MonitoringRun.objects.get_queryset().order_by('-type')
    serializer_class = MonitoringRunSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('type', 'name',)
    search_fields = ('type', 'name',)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMonitoringRunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitoringRun.objects.get_queryset().order_by('id')
    serializer_class = MonitoringRunSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
