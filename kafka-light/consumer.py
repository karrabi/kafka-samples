# consumer/consumer.py
from kafka import KafkaConsumer
import time
import datetime
import logging


# time.sleep(30)
print('Consumer start ...')
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

for message in consumer:
    now = datetime.datetime.now()

    print(f"{now}: Received message: {message.value.decode('utf-8')}")
