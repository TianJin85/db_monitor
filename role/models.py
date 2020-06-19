from django.db import models
from django.utils import timezone
from utils import tools


class RoleList(models.Model):

    role_name = models.CharField('角色名称', max_length=64, blank=True, null=False)
    role_code = models.IntegerField('角色代码', blank=True, null=True)
    role_status = models.IntegerField('角色状态', default=1)  # 1角色启用，0角色禁用
    role_remark = models.CharField('角色备注', max_length=64, blank=True, null=True)
    role_add_date = models.DateTimeField('角色添加日期', default=timezone.now, blank=True, null=True)
    role_update_date = models.DateTimeField('角色修改日期', default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.role_name, self.role_code

    class Meta:
        db_table = 'role_list'
        verbose_name = '角色信息表'
        verbose_name_plural = verbose_name


