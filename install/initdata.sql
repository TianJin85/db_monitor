/*
Navicat MySQL Data Transfer

Source Server         : dbmon
Source Server Version : 50717
Source Host           : 192.168.48.50:3306
Source Database       : db_monitor_dev

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-01-19 17:07:50
*/

INSERT INTO `alarm_conf` VALUES ('1', '1', 'Oracle数据库通断告警', '>=', '1', '连续中断次数', 'oracle_stat', 'select tags,\n       concat(host, \':\', port, \'/\', service_name) url,  \n       concat(tags,\n              \':Oracle数据库通断告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port,\n              \'/\',\n              service_name\n             ) content\n  from oracle_stat\n where status = 1\n and %s>0\n and %s', 'oracle_list', 'alarm_connect');
INSERT INTO `alarm_conf` VALUES ('2', '1', 'Oracle数据库表空间使用率告警', '>=', '90', '使用百分比', 'oracle_tablespace', 'select tags,\n       concat(host, \':\', port, \'/\', service_name) url,  \n       concat(tags,\n              \':Oracle数据库表空间使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port,\n              \'/\',\n              service_name,\n              \'\\n 表空间名：\',\n              tablespace_name,\n              \'\\n 表空间大小(GB)：\',\n              total_size,\n              \'\\n 表空间使用率：\',\n              percent_used,\n              \'%%\',\n              \'\\n 表空间剩余大小(GB)：\',\n              free_size) content\n  from oracle_tablespace\n where percent_used >= %s and free_size<1\n  and %s', 'oracle_list', 'alarm_tablespace');
INSERT INTO `alarm_conf` VALUES ('4', '1', 'Oracle数据库临时表空间告警', '>=', '90', '使用百分比', 'oracle_temp_tablespace', 'select tags,\n       concat(host, \':\', port, \'/\', service_name) url,  \n       concat(tags,\n              \':Oracle数据库临时表空间使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port,\n              \'/\',\n              service_name,\n              \'\\n 临时表空间名：\',\n              temptablespace_name,\n              \'\\n 临时表空间大小(MB)：\',\n              total_size,\n              \'\\n 临时表空间使用率：\',\n              percent_used,\n              \'%%\',\n              \'\\n 临时表空间已使用大小(MB)：\',\n              used_size) content\n  from oracle_temp_tablespace\n where percent_used >= %s and total_size-used_size<1000\n  and %s', 'oracle_list', 'alarm_temp_tablespace');
INSERT INTO `alarm_conf` VALUES ('6', '1', 'Oracle数据库Undo表空间告警', '>=', '90', '使用百分比', 'oracle_undo_tablespace', 'select tags,\n       concat(host, \':\', port, \'/\', service_name) url,  \n       concat(tags,\n              \':Oracle数据库undo表空间使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port,\n              \'/\',\n              service_name,\n              \'\\n undo表空间名：\',\n              undotablespace_name,\n              \'\\n undo表空间大小(MB)：\',\n              total_size,\n              \'\\n undo表空间使用率：\',\n              percent_used,\n              \'%%\',\n              \'\\n undo表空间已使用大小(MB)：\',\n              used_size) content\n  from oracle_undo_tablespace\n where percent_used >= %s and total_size-used_size<1000\n  and %s', 'oracle_list', 'alarm_undo_tablespace');
INSERT INTO `alarm_conf` VALUES ('8', '1', 'Oracle数据库连接数告警', '>=', '90', '使用百分比', 'oracle_stat', 'select tags,\n       concat(host, \':\', port, \'/\', service_name) url,  \n       concat(tags,\n              \':Oracle数据库连接数使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port,\n              \'/\',\n              service_name,\n              \'\\n 最大连接数：\',\n              max_process,\n              \'\\n 当前连接数：\',\n              current_process,\n              \'\\n 连接数使用率：\',\n              process_used_percent,\n              \'%%\') content\n  from oracle_stat\n where process_used_percent >= %s\n  and %s', 'oracle_list', 'alarm_process');
INSERT INTO `alarm_conf` VALUES ('9', '1', 'Oracle数据库adg延迟告警', '>=', '300', '单位：秒', null, 'select tags,\r\n       concat(host, \':\', port, \'/\', service_name) url,  \r\n       concat(tags,\r\n              \':Oracle数据库ADG延迟告警\',\r\n              \'\\n 告警时间：\',\r\n              current_timestamp(),\r\n              \' \\n 数据库url: \',\r\n              host,\r\n              \':\',\r\n              port,\r\n              \'/\',\r\n              service_name,\r\n              \'\\n ADG延迟时间(transport)：\',\r\n              adg_transport_value,\r\n              \'(秒)\',\r\n              \'\\n ADG延迟时间(apply)：\',\r\n              adg_apply_value,\r\n              \'(秒)\') content\r\n  from oracle_db\r\n where length(adg_transport_lag)>0 and length(adg_apply_lag)>0 and\r\n least(adg_transport_value,adg_apply_value) >= %s\r\n  and %s', 'oracle_list', 'alarm_adg');
INSERT INTO `alarm_conf` VALUES ('10', '1', 'Oracle数据库后台日志告警', '>=', '1', '检测后台日志异常', null, 'select tags,\r\n       concat(host, \':\', port, \'/\', service_name) url,  \r\n       concat(tags,\r\n              \':Oracle数据库后台日志告警\',\r\n              \'\\n 告警时间：\',\r\n              current_timestamp(),\r\n              \' \\n 数据库url: \',\r\n              host,\r\n              \':\',\r\n              port,\r\n              \'/\',\r\n              service_name,\r\n              \' \\n 异常信息:\',\r\n              err_info\r\n             ) content\r\n  from oracle_db\r\n where err_info is not null\r\n  and 99>%s\r\n  and %s', 'oracle_list', 'alarm_alert_log');
INSERT INTO `alarm_conf` VALUES ('11', '1', 'Oracle数据库综合性能告警', '>=', '100', '单位时间内等待事件数量', null, 'select tags,\r\n       concat(host, \':\', port, \'/\', service_name) url,\r\n       concat(tags,\r\n              \':Oracle数据库综合性能告警\',\r\n              \'\\n 告警时间：\',\r\n              current_timestamp(),\r\n              \' \\n 数据库url: \',\r\n              host,\r\n              \':\',\r\n              port,\r\n              \'/\',\r\n              service_name,\r\n              \' \\n 等待事件数量:\',\r\n              cnt_all) content\r\n  from (select tags, host, port, service_name, sum(event_cnt) cnt_all\r\n          from oracle_db_event_his\r\n         where timestampdiff(minute, chk_time, current_timestamp()) < 30\r\n         group by tags, host, port, service_name) t\r\n where cnt_all >= %d \r\n  and %s', 'oracle_list', 'alarm_wait_events');
INSERT INTO `alarm_conf` VALUES ('12', '1', 'Oracle数据库pga使用率告警', '>=', '90', '使用百分比', 'oracle_stat', 'select tags,\n       concat(host, \':\', port, \'/\', service_name) url,  \n       concat(tags,\n              \':Oracle数据库PGA使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port,\n              \'/\',\n              service_name,\n              \' \\n PGA使用大小(MB)：\',\n              pga_used_size,\n              \'\\n PGA使用率：\',\n              pga_used_percent,\n              \'%%\') content\n  from oracle_stat\n where pga_used_percent >= %s\n  and %s', 'oracle_list', 'alarm_pga');
INSERT INTO `alarm_conf` VALUES ('13', '1', 'Oracle数据库归档使用率告警', '>=', '90', '使用百分比', 'oracle_stat', 'select tags,\n       concat(host, \':\', port, \'/\', service_name) url,  \n       concat(tags,\n              \':Oracle数据库归档使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port,\n              \'/\',\n              service_name,\n              \'\\n 归档使用率：\',\n              archive_used_percent ,\n              \'%%\') content\n  from oracle_stat\n where archive_used_percent >= %s\n  and %s', 'oracle_list', 'alarm_archive');
INSERT INTO `alarm_conf` VALUES ('14', '1', 'Oracle数据库锁异常告警', '>=', '100', '锁定时间，单位：秒', null, 'select tags,\r\n       concat(host, \':\', port, \'/\', service_name) url,  \r\n       concat(tags,\r\n              \':Oracle数据库锁异常告警\',\r\n              \'\\n 告警时间：\',\r\n              current_timestamp(),\r\n              \' \\n 数据库url: \',\r\n              host,\r\n              \':\',\r\n              port,\r\n              \'/\',\r\n              service_name,\r\n              \'\\n 会话SID：\',\r\n              session_id,\r\n              \'\\n 等待时间：\',\r\n              ctime,\r\n              \'(秒)\',\r\n              \'\\n 锁类型：\',\r\n              type) content\r\n  from oracle_lock\r\n where session like \'Waiter%%\'\r\n and ctime > \'%s\'\r\n  and %s', 'oracle_list', 'alarm_lock');
INSERT INTO `alarm_conf` VALUES ('16', '1', 'Oracle失效索引告警', '>=', '1', '检测失效索引', null, 'select tags,\r\n       concat(host, \':\', port, \'/\', service_name) url,  \r\n       concat(tags,\r\n              \':Oracle数据失效索引告警\',\r\n              \'\\n 告警时间：\',\r\n              current_timestamp(),\r\n              \' \\n 数据库url: \',\r\n              host,\r\n              \':\',\r\n              port,\r\n              \'/\',\r\n              service_name,\r\n              \'\\n 用户名称：\',\r\n              owner,\r\n              \'\\n 索引名称：\',\r\n              index_name,\r\n              \'\\n 分区名称：\',\r\n              partition_name,\r\n              \'\\n 索引状态：\',\r\n              status) content\r\n  from oracle_invalid_index\r\n  and 99>%s\r\n  and %s', 'oracle_list', 'alarm_invalid_index');
INSERT INTO `alarm_conf` VALUES ('17', '4', 'Linux主机通断告警', '>=', '2', '连续中断次数', 'linux_stat', 'select tags,\n       host url,  \n       concat(tags,\n              \':Linux主机通断告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 主机IP: \',\n              host\n             ) content\n  from linux_stat\n where status = 1 and 99 > %s\n  and %s', 'linux_list', 'alarm_connect');
INSERT INTO `alarm_conf` VALUES ('18', '4', 'Linux主机CPU使用率告警', '>=', '90', '使用百分比', 'linux_stat', 'select tags,\n       host url,\n       concat(tags,\n              \':Linux主机CPU使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 主机IP: \',\n              host,\n              \'\\n CPU使用率：\',\n              cpu_used,\n              \'%%\') content\n  from linux_stat\n where cpu_used >= %s\n  and %s', 'linux_list', 'alarm_cpu');
INSERT INTO `alarm_conf` VALUES ('19', '4', 'Linux主机内存使用率告警', '>=', '90', '使用百分比', 'linux_stat', 'select tags,\n       host url,  \n       concat(tags,\n              \':Linux主机内存使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 主机IP: \',\n              host,\n              \'\\n 内存使用率：\',\n              mem_used,\n              \'%%\'\n             ) content\n  from linux_stat\n where mem_used >= %s\n  and %s', 'linux_list', 'alarm_mem');
INSERT INTO `alarm_conf` VALUES ('20', '4', 'Linux主机文件系统使用率告警', '>=', '95', '使用百分比', 'linux_disk', 'select tags,\n       host url,  \n       concat(tags,\n              \':Linux主机磁盘使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 主机IP: \',\n              host,\n              \' \\n 目录名称：\',\n              mount_point,\n              \' \\n 目录总大小(GB)：\',\n              round(total_size/1024,2),\n              \'\\n 目录可用大小(GB)\',\n              round(free_size/1024,2),\n              \'\\n 使用率：\',\n              used_percent,\n              \'%%\'\n             ) content\n  from linux_disk\n where used_percent >= %s\n       and free_size < 5\n  and %s', 'linux_list', 'alarm_disk');
INSERT INTO `alarm_conf` VALUES ('21', '2', 'MySQL数据库通断告警', '>=', '1', '连续中断次数', 'mysql_stat', 'select tags,\n       concat(host, \':\', port) url,  \n       concat(tags,\n              \':MySQL数据库通断告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 数据库url: \',\n              host,\n              \':\',\n              port\n             ) content\n  from mysql_stat\n where status = 1 and 99 > %s\n  and %s', 'mysql_list', 'alarm_connect');
INSERT INTO `alarm_conf` VALUES ('23', '4', 'Linux主机swap使用率告警', '>=', '10', '使用百分比', 'linux_stat', 'select tags,\n       host url,  \n       concat(tags,\n              \':Linux主机SWAP使用率告警\',\n              \'\\n 告警时间：\',\n              current_timestamp(),\n              \' \\n 主机IP: \',\n              host,\n              \'\\n SWAP使用率：\',\n              round(swap_used*100/(swap_used+swap_free),2),\n              \'%%\'\n             ) content\n  from linux_stat\n where (swap_used+swap_free)>0 and swap_used*100/(swap_used+swap_free) >= %s\n  and %s', 'linux_list', 'alarm_swap');
INSERT INTO `alarm_conf` VALUES ('24', '3', 'Redis通断告警', '>=', '1', '连续中断次数', null, 'select tags,\r\n       concat(host, \':\', port) url,  \r\n       concat(tags,\r\n              \':Redis通断告警\',\r\n              \'\\n 告警时间：\',\r\n              current_timestamp(),\r\n              \' \\n Redis url: \',\r\n              host,\r\n              \':\',\r\n              port\r\n             ) content\r\n  from redis\r\n where mon_status = \'connected error\' and 99 > %s\r\n  and %s', 'redis_list', 'alarm_connect');
INSERT INTO `alarm_conf` VALUES ('25', '3', 'Redis内存使用率告警', '>=', '80', '使用百分比', null, 'select tags,\r\n       concat(host, \':\', port) url,  \r\n       concat(tags,\r\n              \':Redis内存使用率告警\',\r\n              \'\\n 告警时间：\',\r\n              current_timestamp(),\r\n              \' \\n Redis url: \',\r\n              host,\r\n              \':\',\r\n              port,\r\n              \' \\n 最大内存配置(MB)\',\r\n              max_memory,\r\n              \' \\n 使用内存大小(MB)\',\r\n              used_memory,\r\n              \' \\n 内存使用率\',\r\n              used_memory_pct,\r\n              \'%%\'\r\n             ) content\r\n  from redis\r\n where used_memory_pct >= %s\r\n  and %s', 'redis_list', 'alarm_mem');

INSERT INTO `django_celery_beat_intervalschedule` VALUES ('1', '10', 'minutes');

INSERT INTO `django_celery_beat_periodictask` VALUES ('3', 'maincheck', 'system.tasks.main_check', '[]', '{}', null, null, null, null, '1', now(), '0', now(), '', null, '1', null, '0', null, null, '{}', null);


SET @@global.sql_mode= '';