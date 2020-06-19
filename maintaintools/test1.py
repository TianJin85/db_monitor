"""
@Time ： 2020/04/24 11:40
@Auth ： 孙权
@File ：test1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

# from mysql.connector import connection

# import pandas as pd

import pymysql.cursors

#
# def logintoserver(request):
#     # req = str(request.body, 'utf-8')
#     req = json.loads(request.body)
#     print(req)
#     allval = []
#     text_commd = ''
#     try:
#
#             # # 实例化SSHClient
#             # client = paramiko.SSHClient()
#             # # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
#             # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             # # 连接SSH服务端，以用户名和密码进行认证
#             # client.connect(hostname='192.168.1.25', port=22, username='root', password='lecent123')
#             # # 打开一个Channel并执行命令
#             # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值，get_pty=True 从服务器请求一个伪终端(默认' ' False ' ')。见“.Channel.get_pty”
#             #ps auxww|grep mysqld|grep -v root|grep -v grep
#            # stdin, stdout, stderr = client.exec_command('ps -ef | grep mysql', get_pty=True)
#             #res, err = stdout.read().decode('utf-8'), stderr.read().decode('utf-8')
#             #print(res)
#
#             # 获取所有pid
#             # pids = psutil.pids()
#             # print(pids)
#
#             #mysql登录
#             try:
#
#                 client.close()
#                 return HttpResponse(json.dumps(tabs),content_type="application/json",)
#             except Exception as e:
#                 return HttpResponse('{"status":"0","message":"数据库连接失败!!","result":"null"}')
#     except Exception as e:
#         print(e)
#         return HttpResponse('{"status":"0","message":"服务器登录失败!!","result":"null"}')

allbase=[]
tabs=[]
conn = pymysql.connect(host='192.168.1.25', user='root', password='root')
# print(conn)
cursor = conn.cursor()
# 获取改服务器下的所有数据库名
cursor.execute('show databases')
result = cursor.fetchall()
# datebase=[]
# for i in result:
#
#     datebase.append([k for k in i])
#
# print([m for m in datebase])
# 进入数据库，获取所有表
# print(result.split(','))
# allbase=[]
# tabs=[]
# for base in result:
# #     for i in base:
# #         allbase.append(i)
# #
# # for db in allbase:
# #     print(db)
# #     connect_sql = 'use' + ' ' + db
# #     cursor.execute(connect_sql)
# #     cursor.execute('show tables')
# #     tables = cursor.fetchall()  # 获得表名，返回数组
# #     for tab in tables:
# #         tabs.append(tab)


for base in result:
    for i in base:

        onnect_sql = 'use' + ' ' + i
        cursor.execute(onnect_sql)
        cursor.execute('show tables')
        tables = cursor.fetchall()  # 获得表名，返回数组

        # for tab in tables:
        #     tabs.append(tab)
        #     print(tab)
# for db in allbase:
#     print(db)
#     connect_sql = 'use' + ' ' + db
#     cursor.execute(connect_sql)
#     cursor.execute('show tables')
#     tables = cursor.fetchall()  # 获得表名，返回数组
#     for tab in tables:
#         tabs.append(tab)
    # break
# print(allbase)
cursor.close()
conn.close()