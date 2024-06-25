import websocket

from kafka import KafkaProducer
import time
import json


brokers = ['kafka1:9092', 'kafka2:9092']

time.sleep(30)

producer = KafkaProducer(
    bootstrap_servers=brokers
    )

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
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:41"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:10026"}')
    ws.send('{"type":"subscribe","symbol":"OANDA:XAU_USD"}')
    ws.send('{"type":"subscribe","symbol":"FXCM:XAU/USD"}')
    ws.send('{"type":"subscribe","symbol":"FXCM:BTC/USD"}')



if __name__ == "__main__":
    
    print('Producer Start ...')
    
    websocket.enableTrace(False)
    while True:
        try:

            ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c5dshh2ad3ifm1hm82s0",
                                    on_message = on_message,
                                    on_error = on_error)
            ws.on_open = on_open
            ws.run_forever()
            
        except Exception as e:
            print(f"Connection lost: {e}. Reconnecting...")
            time.sleep(5)  # Wait for 5 seconds before attempting to reconnect

