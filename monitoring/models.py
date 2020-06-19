from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils import timezone


# Create your models here.


class MonitoringLog(models.Model):
    LOG_LEVEL = [
        ('error', 'error'),
        ('warn', 'warn'),
        ('info', 'info')
    ]

    tags = models.CharField("标签", max_length=32)
    host = models.CharField("主机ip", max_length=32)
    type = models.CharField("采集源类型 1:Oracle数据库 2:MySQL数据库 3:Redis 4:Linux", max_length=16)
    log_time = models.CharField("日志时间", max_length=255)
    log_level = models.CharField("日志级别", max_length=16, choices=LOG_LEVEL)
    log_content = models.TextField("日志内容")
    check_time = models.DateTimeField("采集时间", default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'monitoring_log'
        verbose_name = "日志解析采集数据"
        verbose_name_plural = verbose_name


class MonitoringConfig(models.Model):
    type = models.IntegerField("采集源类型 1:Oracle数据库 2:MySQL数据库 3:Redis 4:Linux")
    name = models.CharField("告警名称", max_length=128)
    judge_sql = models.TextField("判断SQL")
    check_time = models.DateTimeField("添加时间", default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'monitoring_config'
        verbose_name = "SQL配置"
        verbose_name_plural = verbose_name


class MonitoringInfo(models.Model):
    tags = models.CharField("标签", max_length=32)
    url = models.CharField("连接地址", max_length=255)
    alarm_type = models.CharField("告警类型", max_length=255)
    alarm_header = models.CharField("告警标题", max_length=255)
    alarm_content = models.TextField("告警标题", )
    alarm_time = models.DateTimeField("告警时间")

    class Meta:
        db_table = 'monitoring_info'
        verbose_name = "告警信息"
        verbose_name_plural = verbose_name


class MonitoringInfoHis(models.Model):
    tags = models.CharField("标签", max_length=32)
    url = models.CharField("连接地址", max_length=255)
    alarm_type = models.CharField("告警类型", max_length=255)
    alarm_header = models.CharField("告警标题", max_length=255)
    alarm_content = models.TextField("告警标题", )
    alarm_time = models.DateTimeField("告警时间")

    class Meta:
        db_table = 'monitoring_info_his'
        verbose_name = "告警信息"
        verbose_name_plural = verbose_name


class MonitoringRun(models.Model):
    name = models.CharField("SQL检测指标名称", max_length=128)
    monitoring_run_id = models.CharField("SQL检测指标ID", max_length=128)
    mysql_list_id = models.CharField("数据库服务ID", max_length=128)
    database_name = models.CharField("数据库名称", max_length=128)
    check_time = models.DateTimeField("添加时间", default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'monitoring_run'
        verbose_name = "监控运行"
        verbose_name_plural = verbose_name

