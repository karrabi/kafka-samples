import websocket

from kafka import KafkaProducer
import time
import datetime
import logging
import json
import ast

def on_message(ws, message):
    dict_message = json.loads(message)

    for row in dict_message['data']:
        print(row)
        message_bytes = json.dumps(row).encode('utf-8')
        producer.send('test-topic', message_bytes)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:ETHUSDT"}')




producer = KafkaProducer(bootstrap_servers='localhost:9092')

if __name__ == "__main__":
    
    print('Producer Start ...')
    
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bpu4no7rh5red6hq49u0",
                              on_message = on_message,
                              on_error = on_error)
    ws.on_open = on_open
    ws.run_forever()
