# encoding:utf-8
from django.db import models
from django.utils import timezone


# Create your models here.

# app监控列表
class AppList( models.Model ):
    print( "----------------models>AppList-----------------------" )
    app_id = models.CharField( "应用ID", max_length=32, blank=True, null=True )
    app_name = models.CharField( "应用名称", max_length=32, blank=True, null=True )
    app_host = models.CharField( "应用归属服务器", max_length=32 )
    app_type = models.CharField( "应用类型", max_length=256 )
    app_url = models.CharField( "应用路径", max_length=256 )
    app_status = models.IntegerField( "应用连接状态 0离线 1成功", blank=True, null=True )
    app_obj = models.CharField( "项目名称", max_length=32, blank=True, null=True )
    remarks = models.CharField( "备注", max_length=32, blank=True, null=True )
    check_time = models.DateTimeField( "添加时间", default=timezone.now, blank=True, null=True )

    def __str__(self):
        return self.app_name

    class Meta:
        db_table = 'system_app'
        verbose_name = "app信息"
        verbose_name_plural = verbose_name


class AppConfigSetting( models.Model ):
    print( "-------------------------------models>AppConfig----------------" )
    test1 = models.CharField( "", max_length=32 )
    test2 = models.CharField( "", max_length=32 )
    test3 = models.CharField( "", max_length=32 )

    def __str__(self):
        return self.test1

    class Meta:
        db_table = 'app_conf_setting'
        verbose_name = "app配置设置"
        verbose_name_plural = verbose_name
