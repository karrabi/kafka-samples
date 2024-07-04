# consumer/consumer.py
from kafka import KafkaConsumer
import redis
import time
import datetime
import logging
import json
import ast


import psycopg2
from psycopg2 import pool

cache = redis.Redis(host='redis', port=6379, db=0)
brokers = ['kafka1:9092', 'kafka2:9092', 'kafka3:9092']

time.sleep(40)

print('Consumer start ...')
consumer = KafkaConsumer(
    'crypto_topic', 
    bootstrap_servers=brokers,
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))

)
print('Consumer configured ...')


for message in consumer:
    value = message.value
    # print(type(value['s']))
    # print(value['s'])
    # print(type(value['t']))
    # print(value['t'])
    # print(type(value['p']))
    # print(value['p'])

    print(value)
    lkey = f"lastPrice:{str(value['s']).replace(':', '-')}"
    cache.sadd(lkey, float(value['p']))
    hkey = f"historyPrice:{str(value['s']).replace(':', '-')}"
    cache.zadd(hkey, {str(value['t']): float(value['p'])})
    
