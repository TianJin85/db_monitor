# encoding:utf-8
import logging
from .models import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


# Ecs Api           drf 中文文档   http://drf.jiuyou.info/#/drf/requests
class ApiAppList( generics.ListCreateAPIView ):
    print( "----------------views>ApiUserList-----------------------" )
    logger = logging.getLogger( __name__ )
    logger.debug( 'debug message' )
    logger.info( 'info message' )
    logger.warn( 'warn message' )
    logger.error( 'error message' )
    logger.critical( 'critical message' )

    queryset = AppList.objects.get_queryset().order_by( 'id' )
    serializer_class = AppListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'app_name',)
    search_fields = ('id', 'app_name',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiAppDetail( generics.RetrieveUpdateDestroyAPIView ):
    print( "----------------views>ApiUserDetail-----------------------" )
    queryset = AppList.objects.get_queryset().order_by( 'id' )
    serializer_class = AppListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
