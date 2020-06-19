import logging
import re

from django.http import JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from kombu.utils import json

from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from django.core.paginator import Paginator
from role.serializers import *
from role.serializers import RoleListSerializer


# Create your views here.
class ApiRoleList(generics.ListCreateAPIView):
    queryset = RoleList.objects.get_queryset().order_by('id')
    serializer_class = RoleListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('role_name', 'role_code','role_remark',)
    search_fields = ('role_name', 'role_code','role_remark',)
    ordering_fields = ('role_name', 'role_code','role_remark',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    print("----------------views>ApiRoleDetail-----------------------")
    queryset = RoleList.objects.get_queryset().order_by('id')
    # queryset = RoleList.objects.get_queryset().order_by('role_code')
    serializer_class = RoleListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class PageInfo:
    """
        :param startRow 当前页码
        :param count 要分页的数据
        :param page_size 每页显示条数
    """

    def __init__(self, count, startRow=1, page_size=10):
        self.count = count
        self.startRow = startRow
        self.page_size = page_size
        self.all_page = self.get_all_page()

    def get_all_page(self):
        """计算总页数"""
        result, mod = divmod(len(self.count), self.page_size)
        if mod:
            return result + 1
        else:
            return result



# 分页处理
def PageLimit(request, pagenum):
    queryset = RoleList.objects.all()
    print('当前对象总个数', queryset)
    # 每页显示的个数
    page_index = request.GET.get('page_size')
    print('获取请求参数', page_index)
    paginator = Paginator(queryset, page_index)
    print('获取所有数据列表', paginator)
    page = paginator.page(pagenum)
    print('分页数据', page)
    data = {
        # 当前页的博文对象列表
        'page': page,
        # 分页页码范围
        'count': paginator.page_range,
        # 当前页的页码
        'page_size': page.number,
    }  # 将数据丢给页面渲染
    return render(request, 'blogs.html', context=data)
