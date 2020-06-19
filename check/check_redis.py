# encoding: utf-8

import time

import redis

import check.checklog as checklog
from check.redis_logparser import get_redis_log
from check.redis_stat import RedisStat
from utils.tools import *


def check_redis(tags, redis_params):
    check_time = now()
    host = redis_params['host']
    port = redis_params['port']
    version = redis_params['version']
    password = redis_params['password']
    linux_params = {
        'hostname': redis_params['host'],
        'port': redis_params['sshport_os'],
        'username': redis_params['user_os'],
        'password': redis_params['password_os']
    }
    # create connection
    redis_conn = redis.StrictRedis(host=host, port=port, password=password)

    if redis_conn:
        the_redis = RedisStat(redis_conn)
        the_redis.get_redis_stat()
        time.sleep(1)
        the_redis.get_redis_stat()
        the_redis.get_redis_config()
        redis_data = the_redis.res
        redis_info = redis_data['info']
        redis_stat = redis_data['stat']
        redis_config = redis_data['config']
        updays = redis_info['uptime_in_days']
        slaves = redis_info['connected_slaves']
        used_memory = round(float(redis_info['used_memory_rss'])/1024/1024,2)
        hits_all = redis_info['keyspace_hits']
        misses_all = redis_info['keyspace_misses']
        hits = redis_stat['keyspace_hits']
        misses = redis_stat['keyspace_misses']
        command_count = redis_stat['total_commands_processed']
        aof_delayed_fsync = 0
        net_input_byte = redis_stat['total_net_input_bytes']
        net_out_byte = redis_stat['total_net_output_bytes']
        redis_commandstats = redis_data['commandstats']

        cmdstat_brpop=0
        cmdstat_publish=0
        cmdstat_setnx=0
        cmdstat_exec=0
        cmdstat_multi=0

        checklog.logger.info('{}：写入redis采集数据' .format(tags))
        clear_table(tags,'redis_stat')

        insert_data_sql = "insert into redis_stat(tags,host,port,version,redis_mode,role,updays,slaves,maxmemory,used_memory," \
                          "mem_fragmentation_ratio,total_keys,expire_keys,connected_clients,hits_all,misses_all,expired_keys,evicted_keys,hits,misses," \
                          "command_count,net_input_byte,net_out_byte,aof_delayed_fsync,cmdstat_brpop,cmdstat_publish,cmdstat_setnx," \
                          "cmdstat_exec,cmdstat_multi,status,check_time) " \
                          "values ('{tags}','{host}','{port}','{version}','{redis_mode}','{role}',{updays},{slaves},{maxmemory},{used_memory}," \
                          "{mem_fragmentation_ratio},{total_keys},{expire_keys},{connected_clients},{hits_all},{misses_all},{expired_keys},{evicted_keys},{hits},{misses}," \
                          "{command_count},{net_input_byte},{net_out_byte},{aof_delayed_fsync},{cmdstat_brpop},{cmdstat_publish},{cmdstat_setnx}," \
                          "{cmdstat_exec},{cmdstat_multi},0,'{check_time}' )"

        insert_data_values = {**redis_info,**redis_stat,**redis_commandstats,**redis_config,**locals()}
        insert_sql = insert_data_sql.format(**insert_data_values)
        print(">>>>>>>>insert_sql>>>>>>>>>>" + insert_sql)
        mysql_exec(insert_sql)
        archive_table(tags,'redis_stat')
        # 后台日志
        get_redis_log(tags, redis_params, linux_params)


if __name__ == '__main__':
    redis_params = {
        'host':'114.116.16.6',
        'port':6379,
        'password':'123qwe',
        'version':'',
        'sshport_os':22,
        'user_os':'root',
        'password_os':'lecent.test'
    }
    check_redis('redis-6379',redis_params)
