# consumer/consumer.py
from kafka import KafkaConsumer
import time
import datetime
import logging
import json
import ast

# time.sleep(30)
print('Consumer start ...')
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))

)

for message in consumer:
    now = datetime.datetime.now()
    message_dict = message.value
    print(f"{now}: Received message: {message_dict}")
