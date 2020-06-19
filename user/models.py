# encoding:utf-8
from django.db import models
from django.utils import timezone
from utils import tools


# Create your models here.

# User监控列表
class UserList(models.Model):
    user_id = models.CharField("用户信息", max_length=32, blank=True, null=True)
    user_name = models.CharField("姓名", max_length=32, blank=True, null=True)
    department = models.CharField("部门", max_length=32, blank=True, null=True)
    permission_group = models.CharField("权限组", max_length=32, blank=True, null=True)
    birthday = models.CharField("生日", max_length=32, blank=True, null=True)
    office_phone = models.CharField("联系方式", max_length=32, blank=True, null=True)
    mail = models.CharField("E-mail", max_length=32, blank=True, null=True)
    fax = models.CharField("传真", max_length=32, blank=True, null=True)
    remarks = models.CharField("备注", max_length=32, blank=True, null=True)
    check_time = models.DateTimeField("添加时间", default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'admin_user'
        verbose_name = "User信息"
        verbose_name_plural = verbose_name
