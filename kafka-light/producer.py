# producer/producer.py
from kafka import KafkaProducer
import time
import datetime
import logging


# time.sleep(30)
print('Producer Start ...')
producer = KafkaProducer(bootstrap_servers='localhost:9092')
i = 1
while True:
    now = datetime.datetime.now()
    print(f'Sending message {i} ...')
    producer.send('test-topic', b'Hello, Kafka!')
    print("Message sent")
    time.sleep(5)
    i += 1
