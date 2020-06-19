from django.http import HttpResponse
from django.shortcuts import render

from utils.mysql_base import MysqlBase
from utils.mysql_base import MysqlBase
from utils.linux_base import LinuxBase
from user.models import UserList
def hello(request):
    mysql_params = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root123'
    }
    sql = "show DATABASES"

    testdate = MysqlBase(mysql_params).query(sql)
    #UserList.objects.create(name="John Fourkas").save()
    #LinuxBase.connection().

    lucifer = UserList.objects.create(user_name="luciferdfd").save()

    print('===========================send============================================')
    print(testdate)
    print('===========================end============================================')
    return render(request, 'web_ssh.html')
