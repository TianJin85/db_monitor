import json

import paramiko
from django.http import HttpResponse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions

from maintaintools.serializers import *


# Create your views here.
class ApiMaintainCommandList(generics.ListCreateAPIView):
    queryset = MaintainCommand.objects.get_queryset().order_by('id')
    serializer_class = MaintainToolsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('commname', 'usecommand',)  # 前台传值进行匹配搜索
    search_fields = ('commname', 'usecommand',)
    ordering_fields = ('commname', 'usecommand',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiMaintainCommandDetail(generics.RetrieveUpdateDestroyAPIView):
    print("----------------views>ApiRoleDetail-----------------------")
    queryset = MaintainCommand.objects.get_queryset().order_by('id')
    serializer_class = MaintainToolsSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class GetPaerm(View):
    def post(self, request, ssh_id):
        queryset = MaintainCommand.objects.get(id=ssh_id)
        ssh_cmd = queryset.usecommand + ' ' + queryset.commandparam
        val = json.loads(request.body)
        allval = []
        text_commd = ''
        for i in val:
            allval.append(i)
        for val in allval:
            host = val.get('host')
            sshport = val.get('sshport')
            user = val.get('user')
            password = val.get('password')
            tags = val.get('tags')
            # 实例化SSHClient
            client = paramiko.SSHClient()
            # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                # 连接SSH服务端，以用户名和密码进行认证
                client.connect(hostname=host, port=sshport, username=user, password=password)
                # 打开一个Channel并执行命令
                # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值，get_pty=True 从服务器请求一个伪终端(默认' ' False ' ')。见“.Channel.get_pty”
                stdin, stdout, stderr = client.exec_command(ssh_cmd, get_pty=True)
                # 打印执行结果
                # text_commd = str(text_commd + '\t\t\t{}\n' + stdout.read().decode('utf-8')).format(tags)#第一方案
                res, err = stdout.read().decode('utf-8'), stderr.read().decode('utf-8')  # 第二方案
                text_commd = str(text_commd + '\t\t\t{}\n' + res if res else err).format(tags)
                # 关闭SSHClient
                client.close()
            except Exception as e:
                print(tags, '服务器连接失败！请检查登录的用户名密码是否正确！！')
                print(e)

            # print('数据库保存开始')
            sshalldate = SshExecCommand.objects.create(tags=tags, host=host, sshport=sshport, user=user,
                                                       password=password, ssh_cmd=ssh_cmd, execresult=text_commd)

            sshalldate.save()
        return HttpResponse(text_commd)


# 文件上传后的记录表
class ApiUploadDownFileList(generics.ListCreateAPIView):
    queryset = UploadDownFileInfo.objects.get_queryset().order_by('id')
    serializer_class = UploadFileSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('file_name',)  # 前台传值进行匹配搜索
    search_fields = ('file_name',)
    ordering_fields = ('file_name',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限
    print('12333333333333')
    def uploadfile(self, request, file):
        print('5555555555555555555555')
        hostval=json.loads(request.body)
        print(hostval)
        print(file)
        if request.method == 'POST' and request.FILES.get(file):
            from django.core.files.storage import FileSystemStorage
            myfile = request.FILES[file]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            print(filename)
