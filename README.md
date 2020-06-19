
# DB monitor数据库监控平台

![](https://img.shields.io/badge/build-release-brightgreen.svg)
![](https://img.shields.io/badge/version-v1.0.0-brightgreen.svg)
![](https://img.shields.io/badge/vue.js-2.9.6-brightgreen.svg)
![](https://img.shields.io/badge/iview-3.4.0-brightgreen.svg?style=flat-square)
![](https://img.shields.io/badge/python-3.6-brightgreen.svg)
![](https://img.shields.io/badge/Django-2.2-brightgreen.svg)


后端：https://github.com/zxb1987/db_monitor.git
## 特性
- **构建**: 前后端分离架构，Python+Django+restframework提供后台API，celery定制数据采集策略，Iview作为前端展示
- **UI**: 开箱即用的高质量前端设计，提供丰富的图表、指标展示，核心数据形成趋势图分析
- **深度定制**: 提供完整可用的数据监控方案，告别冗长的SQL脚本、常用手册，复杂数据通过web页面即可轻易浏览

## 功能简介

- 资源管理
    - 支持Oracle/MySQL/Redis/Linux资源情况录入，涵盖大部分日常所需信息，形成完整资产库
    - 资源管理中各类设备信息作为采集设备来源，支持动态加入实例监控列表
    
...待补充

## 环境

- Python 3.6
    - Django 2.2
    - Django Rest Framework 3.1
    
- Vue.js 2.9
    - iview 3.4
    
快速开始
===============
###  平台使用
- [在线访问](http://114.116.16.6:9992/) (推荐使用chrome浏览器访问)
  
| 账号 | 密码 |
| --- | --- |
| admin | 123qwe |


## 安装部署
#### 1. 安装python3.6(略)

#### 2. 安装mysql5.7(略)

注意字符集：utf-8

create database db_monitor; 

#### 3. 安装redis3.2(略)

#### 4. 安装oracle instant client(略)

#### 5. 项目配置

##### 下载源代码
git clone https://github.com/zxb1987/db_monitor

##### 安装依赖包
pip install -r requirements.txt

##### setting配置
MySQL数据库：

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
		'NAME': 'db_monitor',  
		'USER': 'root',  
		'PASSWORD': 'mysqld',  
        'HOST':'127.0.0.1',  
		'PORT': '3306',  
    }
}

Redis：

CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

CELERY_BROKER_URL = 'redis://localhost:6379/2'

##### 创建数据库
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser(创建登录用户)

##### 执行数据库脚本

@install/initdata.sql

#### 6. 启动
python manage.py runserver
nohup python3 manage.py runserver 0.0.0.0:9998&
nohup python3 manage.py runserver 0.0.0.0:8000&
celery –A db_monitor worker –l info

celery –A db_monitor beat –l info




#### 7. 前端配置
请参考：[db_monitor_vue](https://github.com/zxb1987/db_monitor_vue)

#### 8. oracle数据库监控
对Oracle数据库监控，请在被监控端建立用户，并执行install/sqlscripts(forOracle)中的脚本

grant.sql & table.sql & procedure.sql

## 界面展示

- 资产管理

![demo1](images/demo1.jpg)

- Oracle数据库概览

![demo1](images/demo2.jpg)

- oracle top sql

![demo1](images/demo6.jpg)

- MySQL数据库日志解析

![demo1](images/demo3.jpg)

- 告警记录

![demo1](images/demo4.jpg)

- 告警配置

![demo1](images/demo5.jpg)


## 交流学习
- QQ群 693147566

贡献者
===============
![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/0)![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/1)![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/2)![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/3)![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/4)![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/5)![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/6)![](https://sourcerer.io/fame/hhyo/hhyo/archery/images/7)

Copyright © 2019 DB monitor







sed -i 's/\r$//' start.sh 
杀进程用:
ps aux | grep python3 |  awk '{print $2}' | xargs kill -9
ps -aux | grep python3 | awk '{print $2}' | xargs kill
遇到celery问题
{
终端： 
export PATH=/usr/local/python3/bin:$PATH      # 我的Python3资源文件都放在 /usr/local/python3 文件夹下
  终端： 
sudo echo 'export PATH=/usr/local/python3/bin:$PATH' >> /etc/profile.d/python3.sh  # 避免重启丢失
}

python3 manage.py runserver 0.0.0.0:9998 &9998

select round(b.value / 1024 / 1024, 1) pga_target,
       round(a.pga_used_mb, 1),
       round(a.pga_used_mb / (b.value / 1024 / 1024), 1) * 100  pga_used_pct
  from (select sum(PGA_ALLOC_MEM) / 1024 / 1024 pga_used_mb from v$process) a,
       v$parameter b
 where b.name = 'pga_aggregate_target'



nohup python3 run.py&



http://codingdict.com/sources/py/rest_framework.parsers/18886.html