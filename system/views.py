import json
import logging

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from system.models import Users
from .models import AlertLog, AlarmConf, AlarmInfo
from .serializers import AlertLogSerializer, AlarmConfSerializer, AlarmInfoSerializer

logger = logging.getLogger('system')


class UserInfo(APIView):
    """
    获取用户信息
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        token = (json.loads(request.body))['token']
        obj = Token.objects.get(key=token).user
        result = {
            'name': obj.username,
            'user_id': obj.id,
            'access': list(obj.get_all_permissions()) + ['admin'] if obj.is_superuser else list(
                obj.get_all_permissions()),
            'token': token,
            'avatar': 'https://file.iviewui.com/dist/a0e88e83800f138b94d2414621bd9704.png'
        }
        return HttpResponse(json.dumps(result))
class UserLogout(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        token = (json.loads(request.body))['token']
        obj = Token.objects.get(key=token)
        obj.delete()
        result = {
            "status": True
        }
        return HttpResponse(json.dumps(result))


class CustomBackend(ModelBackend):
    """
    用户名字/邮箱名字 登录
    :param request:
    :return:
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Users.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            logger.error(e)
            return None


class Menu(APIView):
    def post(self, request):
        result = [
            {
                "path": '/assets',
                "name": 'assets',
                "meta": {
                    "icon": 'ios-cloud',
                    "title": '主机管理'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'linux-list',
                        'name': 'linux-list',
                        'meta': {
                            'access': ['assets.view_linuxlist'],
                            'icon': 'ios-menu',
                            'title': 'Linux服务器'
                        },
                        'component': 'assets/linux-list'
                    },
                    {
                        'path': 'oracle-list',
                        'name': 'oracle-list',
                        'meta': {
                            'access': ['assets.view_oraclelist'],
                            'icon': 'ios-menu',
                            'title': 'Oracle数据库'
                        },
                        'component': 'assets/oracle-list'
                    },
                    {
                        'path': 'mysql-list',
                        'name': 'mysql-list',
                        'meta': {
                            'access': ['assets.view_mysqllist'],
                            'icon': 'ios-menu',
                            'title': 'MySql数据库'
                        },
                        'component': 'assets/mysql-list'
                    },
                    {
                        'path': 'redis-list',
                        'name': 'redis-list',
                        'meta': {
                            'access': ['assets.view_redislist'],
                            'icon': 'ios-menu',
                            'title': 'Redis缓存库'
                        },
                        'component': 'assets/redis-list'
                    }
                ]
            },
            {
                "path": '/monlist',
                "name": '实例列表',
                "meta": {
                    "icon": 'ios-apps',
                    "title": '实例列表'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'linux',
                        'name': 'linux',
                        'meta': {
                            'icon': 'ios-menu',
                            'title': 'Linux列表',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'linux/stat-list'
                    },
                    {
                        'path': 'oracle',
                        'name': 'oracle',
                        'meta': {
                            'icon': 'ios-menu',
                            'title': 'Oracle列表',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'oracle/stat-list'
                    },
                    {
                        'path': 'mysql',
                        'name': 'mysql',
                        'meta': {
                            'icon': 'ios-menu',
                            'title': 'MySql列表',
                            'access': ['mysql.view_mysqlstat'],
                        },
                        'component': 'mysql/stat-list'
                    },
                    {
                        'path': 'redis',
                        'name': 'redis',
                        'meta': {
                            'icon': 'ios-menu',
                            'title': 'Redis列表',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/stat-list'
                    }
                ],
            },
            {
                "path": '/alarm',
                "name": 'alarm',
                "meta": {
                    "icon": 'ios-cloud',
                    "title": '服务监控'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'alarm-info',
                        'name': 'alarm-info',
                        'meta': {
                            'access': ['system.view_alarminfo'],
                            'icon': 'ios-menu',
                            'title': '告警记录'
                        },
                        'component': 'system/alarm-info'
                    },
                    {
                        'path': 'alarm-conf',
                        'name': 'alarm-conf',
                        'meta': {
                            'access': ['system.view_alarmconf'],
                            'icon': 'ios-menu',
                            'title': '告警配置'
                        },
                        'component': 'system/alarm-conf'
                    }
                ]
            },
            {
                "path": '/monitoring',
                "name": 'monitoring',
                "meta": {
                    "icon": 'ios-cloud',
                    "title": 'SQL监控'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'monitoring-confing',
                        'name': 'monitoring-confing',
                        'meta': {
                            'access': ['monitoring.view_monitoringconfig'],
                            'icon': 'ios-menu',
                            'title': 'SQL配置'
                        },
                        'component': 'monitoring/monitoring-config'
                    },
                    {
                        'path': 'monitoring-querying',
                        'name': 'monitoring-querying',
                        'meta': {
                            'access': ['monitoring.view_monitoringconfig'],
                            'icon': 'ios-menu',
                            'title': '在线查询'
                        },
                        'component': 'monitoring/monitoring-querying'
                    },
                    {
                        'path': 'monitoring-run',
                        'name': 'monitoring-run',
                        'meta': {
                            'access': ['monitoring.view_monitoringrun'],
                            'icon': 'ios-menu',
                            'title': '监控配置'
                        },
                        'component': 'monitoring/monitoring-run'
                    },
                    {
                        'path': 'monitoring-info',
                        'name': 'monitoring-info',
                        'meta': {
                            'access': ['monitoring.view_monitoringinfo'],
                            'icon': 'ios-menu',
                            'title': '监控记录'
                        },
                        'component': 'monitoring/monitoring-info'
                    },

                ]
            },
            {
                "path": '/maintaintools',
                "name": 'maintaintools',
                "meta": {
                    "icon": 'ios-cloud',
                    "title": '运维工具'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'command-list',
                        'name': 'command-list',
                        'meta': {
                            'access': ['maintaintools.view_maintaincommand'],
                            'icon': 'ios-menu',
                            'title': '命令控制台'
                        },
                        'component': 'maintaintools/command-list'
                    },
                    {
                        'path': 'maintaintools-file',
                        'name': 'maintaintools-file',
                        'meta': {
                            'access': ['maintaintools.view_maintaincommand'],
                            'icon': 'ios-menu',
                            'title': 'ssh文件管理'
                        },
                        'component': 'maintaintools/manageinfo-file'
                    },
                    {
                        'path': 'test',
                        'name': 'test',
                        'meta': {
                            'access': ['maintaintools.view_uploaddownfileinfo'],
                            'icon': 'ios-menu',
                            'title': '测试专用页面'
                        },
                        'component': 'maintaintools/test'
                    },
                ]
            },

            {
                "path": '/app',
                "name": 'app',
                "meta": {
                    "icon": 'ios-cloud',
                    "title": '应用信息'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'app-config',
                        'name': 'app-config',
                        'meta': {
                            'access': ['app.view_applist'],
                            'icon': 'ios-menu',
                            'title': '应用配置'
                        },
                        'component': 'app/app-config'
                    },
                    {
                        'path': 'app-info',
                        'name': 'app-info',
                        'meta': {
                            'access': ['app.view_applist'],
                            'icon': 'ios-menu',
                            'title': '应用信息'
                        },
                        'component': 'app/app-info'
                    }
                ]
            },
            {
                "path": '/report',
                "name": 'report',
                "meta": {
                    "icon": 'ios-cloud',
                    "title": '报告信息'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'business-report-list',
                        'name': 'business-report-list',
                        'meta': {
                            'access': ['assets.view_mysqllist'],
                            'icon': 'ios-menu',
                            'title': '应用报告'
                        },
                        'component': 'user/user-list'
                    },
                    {
                        'path': 'system-report-list',
                        'name': 'system-report-list',
                        'meta': {
                            'access': ['assets.view_mysqllist'],
                            'icon': 'ios-menu',
                            'title': '系统报告'
                        },
                        'component': 'user/role-list'
                    }
                ]
            },

            {
                "path": '/user',
                "name": 'user',
                "meta": {
                    "icon": 'ios-cloud',
                    "title": '系统管理'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'user-list',
                        'name': 'user-list',
                        'meta': {
                            'access': ['user.view_userlist'],
                            'icon': 'ios-menu',
                            'title': '用户管理'
                        },
                        'component': 'user/user-list'
                    },
                    {
                        'path': 'role-list',
                        'name': 'role-list',
                        'meta': {
                            # 后台APP所在文件夹，view_app访问model，view是固定格式
                            'access': ['role.view_rolelist'],
                            'icon': 'ios-menu',
                            'title': '角色管理'
                        },
                        # 传到前端的访问地址
                        'component': 'user/role-list'
                    },
                    {
                        'path': 'permissions-list',
                        'name': 'permissions-list',
                        'meta': {
                            'access': ['assets.view_mysqllist'],
                            'icon': 'ios-menu',
                            'title': '权限管理'
                        },
                        'component': 'user/permissions-list'
                    },
                    {
                        'path': 'resource-list',
                        'name': 'resource-list',
                        'meta': {
                            'access': ['assets.view_mysqllist'],
                            'icon': 'ios-menu',
                            'title': '资源管理'
                        },
                        'component': 'user/resource-list'
                    }
                ]
            },
            {
                "path": '/oracle',
                "name": 'Oracle',
                "meta": {
                    'hideInMenu': 'true',
                    "icon": 'ios-apps',
                    "title": 'Oracle数据库监控'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': ':tags/view',
                        'name': 'oracle-view',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'Oracle概览',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'oracle/view'
                    },
                    {
                        'path': ':tags/resource',
                        'name': 'oracle-resource',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '资源',
                            'access': ['oracle.view_oracletablespace'],
                        },
                        'component': 'oracle/resource'
                    },
                    {
                        'path': ':tags/resource/tablespace/:tablespace_name',
                        'name': 'oracle-tablespace',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '表空间',
                            'access': ['oracle.view_oracletablespace'],
                        },
                        'component': 'oracle/tablespace'
                    },
                    {
                        'path': ':tags/resource/temptablespace/:tablespace_name',
                        'name': 'oracle-temptablespace',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '临时表空间',
                            'access': ['oracle.view_oracletablespace'],
                        },
                        'component': 'oracle/temp-tablespace'
                    },
                    {
                        'path': ':tags/resource/undotablespace/:tablespace_name',
                        'name': 'oracle-undotablespace',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'UNDO表空间',
                            'access': ['oracle.view_oracletablespace'],
                        },
                        'component': 'oracle/undo-tablespace'
                    },
                    {
                        'path': ':tags/active-session',
                        'name': 'oracle-active-session',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '活动会话',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'oracle/active-session'
                    },
                    {
                        'path': ':tags/performance',
                        'name': 'oracle-performance',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '性能图',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'oracle/performance'
                    },
                    {
                        'path': ':tags/top-sql',
                        'name': 'oracle-top-sql',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'TOP SQL',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'oracle/top-sql'
                    },
                    {
                        'path': ':tags/alert-log',
                        'name': 'oracle-alertlog',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '日志解析',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'oracle/alert-log'
                    },
                    {
                        'path': ':tags/table-stats',
                        'name': 'oracle-tablestats',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '统计信息',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'oracle/table-stats'
                    }

                ],

            },
            {
                "path": '/linux',
                "name": 'Linux',
                "meta": {
                    'hideInMenu': 'true',
                    "icon": 'ios-apps',
                    "title": 'Linux主机监控'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': ':tags/view',
                        'name': 'linux-view',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'Linux概览',
                            'access': ['linux.view_linuxstat'],
                        },
                        'component': 'linux/view'
                    },
                    {
                        'path': ':tags/io',
                        'name': 'linux-io',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '磁盘IO',
                            'access': ['linux.view_linuxstat'],
                        },
                        'component': 'linux/io'
                    },
                    {
                        'path': ':tags/memory',
                        'name': 'linux-memory',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '内存&虚拟内存',
                            'access': ['linux.view_linuxstat'],
                        },
                        'component': 'linux/memory'
                    }
                ]
            },
            {
                "path": '/mysql',
                "name": 'MySQL',
                "meta": {
                    'hideInMenu': 'true',
                    "icon": 'ios-apps',
                    "title": 'MySQL数据库监控'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': ':tags/view',
                        'name': 'mysql-view',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'MySQL概览',
                            'access': ['mysql.view_mysqlstat'],
                        },
                        'component': 'mysql/view'
                    },
                    {
                        'path': ':tags/myisam',
                        'name': 'mysql-myisam',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'MyISAM',
                            'access': ['mysql.view_mysqlstat'],
                        },
                        'component': 'mysql/myisam'
                    },
                    {
                        'path': ':tags/innodb',
                        'name': 'mysql-innodb',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'Innodb',
                            'access': ['mysql.view_mysqlstat'],
                        },
                        'component': 'mysql/innodb'
                    },
                    {
                        'path': ':tags/alert-log',
                        'name': 'mysql-alert-log',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '后台日志',
                            'access': ['mysql.view_mysqlstat'],
                        },
                        'component': 'mysql/alert-log'
                    },
                    {
                        'path': ':tags/slowquery-log',
                        'name': 'mysql-slowquery-log',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '慢查询',
                            'access': ['mysql.view_mysqlstat'],
                        },
                        'component': 'mysql/slowquery-log'
                    }
                ]

            },
            {
                "path": '/redis',
                "name": 'Redis',
                "meta": {
                    'hideInMenu': 'true',
                    "icon": 'ios-apps',
                    "title": 'Redis监控'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': ':tags/view',
                        'name': 'redis-view',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'Redis概览',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/view'
                    },
                    {
                        'path': ':tags/immediate-stats',
                        'name': 'redis-immediate-stats',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'Redis实时状态',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/immediate-stats'
                    },
                    {
                        'path': ':tags/config',
                        'name': 'redis-config',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'Redis配置项',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/config'
                    },
                    {
                        'path': ':tags/slowlog',
                        'name': 'redis-slowlog',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '慢查询分析',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/slowlog'
                    },
                    {
                        'path': ':tags/clientlist',
                        'name': 'redis-clientlist',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '连接信息',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/clientlist'
                    },
                    {
                        'path': ':tags/commandstats',
                        'name': 'redis-commandstats',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '命令曲线',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/command-stats'
                    },
                    {
                        'path': ':tags/alert-log',
                        'name': 'redis-alert-log',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '后台日志',
                            'access': ['rds.view_redisstat'],
                        },
                        'component': 'redis/alert-log'
                    },
                ]

            }
            # {
            #     "path": '/multilevel',
            #     "name": 'multilevel',
            #     "meta": {
            #         "icon": 'md-menu',
            #         "title": '多级菜单'
            #     },
            #     "component": 'Main',
            #     "children": [
            #         {
            #             "path": '/level_2_1',
            #             "name": 'level_2_1',
            #             "meta": {
            #                 "icon": 'md-funnel',
            #                 "title": '二级-1'
            #             },
            #             "component": 'multilevel/level-2-1'
            #         },
            #
            #     ]
            # },
        ]
        return HttpResponse(json.dumps(result))


class ApiAlertLog(generics.ListAPIView):
    queryset = AlertLog.objects.all().order_by('-log_time')
    serializer_class = AlertLogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['tags', 'log_level']
    search_fields = ['log_content']
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiAlarmConf(generics.ListCreateAPIView):
    queryset = AlarmConf.objects.get_queryset().order_by('-type')
    serializer_class = AlarmConfSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('type', 'name',)
    search_fields = ('type', 'name',)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiAlarmConfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlarmConf.objects.get_queryset().order_by('id')
    serializer_class = AlarmConfSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiAlarmInfo(generics.ListCreateAPIView):
    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        if tags:
            return AlarmInfo.objects.filter(tags=tags).order_by('id')
        else:
            return AlarmInfo.objects.all()

    serializer_class = AlarmInfoSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiAlarmInfoHis(generics.ListCreateAPIView):
    queryset = AlarmInfo.objects.get_queryset().order_by('-id')
    serializer_class = AlarmInfoSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags',)
    search_fields = ('tags', 'alarm_content',)
    permission_classes = (permissions.DjangoModelPermissions,)
