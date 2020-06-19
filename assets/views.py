# encoding:utf-8
import simplejson
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from django.views.generic import View
from utils.utils import *
from utils.parser import Argument, JsonParser
from .serializers import *
import json
from datetime import datetime
import os

# Ecs Api           drf 中文文档   http://drf.jiuyou.info/#/drf/requests
class ApiOracleList(generics.ListCreateAPIView):
    queryset = OracleList.objects.get_queryset().order_by('id')
    serializer_class = OracleListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host', 'db_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiOracleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OracleList.objects.get_queryset().order_by('id')
    serializer_class = OracleListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMysqlList(generics.ListCreateAPIView):
    queryset = MysqlList.objects.get_queryset().order_by('id')
    serializer_class = MysqlListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host', 'db_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiMysqlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MysqlList.objects.get_queryset().order_by('id')
    serializer_class = MysqlListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiLinuxList(generics.ListCreateAPIView):
    queryset = LinuxList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host', 'linux_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiLinuxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinuxList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiRedisList(generics.ListCreateAPIView):
    queryset = RedisList.objects.get_queryset().order_by('id')
    serializer_class = RedisListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host', 'redis_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiRedisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RedisList.objects.get_queryset().order_by('id')
    serializer_class = RedisListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


def web_ssh(request):
    form, error = JsonParser(

    ).parse(request.POST)
    print(form.id)

    for k, v in request.GET.items():
        print(k)
        # val=json.loads()
        # print(val)

    # #queryset = LinuxList.objects.filter(pk=h_id).last()
    # print("------------------")
    # #print(h_id)
    # print("=============")
    # # print(host)
    # # if not host:
    #     return HttpResponseBadRequest('unknown host')
    # context = {'id': h_id, 'title': host.name, 'token': request.user.access_token}
    # return render(request, 'web_ssh.html', context)


class AppView(View):
    def get(self, request, h_id):
        return json_response("{'name:'get}")

    # def post(self, request):
    #
    #     # form, error = JSONParser(
    #     #
    #     # ).parse(request.body)
    #     print(request.body)
    #     for k, v in request.POST.items():
    #        print(k,"---", v)
    #     return json_response("{'name:'post}")

    def post(self, request):
        print('========requestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequest==========')
        image = request.FILES.get('image')
        image_name = datetime.now().strftime('%Y%m%d%H%M%S%f') + image.name
        f = open(os.path.join("templates", image_name), 'wb')
        #以二进制流写入文件
        for i in image.chunks():
            f.write(i)
        f.close()













        # print(request.body)
        # receive_data = simplejson.loads(request.body)
        # print(receive_data)
        #
        # receive_data = json.loads(request.body.decode())
        #
        # print(receive_data["user"]["name"])
        # print(receive_data["password"])
        return HttpResponse('OK')

    def put(self, request):
        form, error = JsonParser(
            Argument('tags', required=False),
            Argument('host', required=False),
            Argument('hostname', required=False),
        ).parse(request.body)

        # tags: '',
        # host: '',
        # hostname: '',
        print(form)

        return json_response(error="sadsads")

    def patch(self, request):
        return json_response("{'name:'patch}")

    def delete(self, request, r_id):
        form, error = JsonParser(
            Argument('id', type=int, help='请指定操作对象')
        ).parse(request.body)

        obj = LinuxList.objects.get(id="1")
        print(obj)

        receive_data = json.loads(request.body.decode())

        print(receive_data)
        print(error)
        print('==================')
        print(form)
        if error is None:
           print(error)

        return json_response(error=error)
