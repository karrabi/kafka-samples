import websocket

from kafka import KafkaProducer
import time
import json

brokers = ['kafka1:9092', 'kafka2:9092', 'kafka3:9092']

time.sleep(40)

producer = KafkaProducer(
    bootstrap_servers=brokers
    )



def on_message(ws, message):
    try:
        dict_message = json.loads(message)

        for row in dict_message['data']:
            print(row)
            message_bytes = json.dumps(row).encode('utf-8')
            producer.send('crypto_topic', message_bytes)
    except Exception as e:
        print(e)
        print(message)


def on_error(ws, error):
    print(f'Error: {error}')

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"KUCOIN:BTC-USDT"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:ETHUSDT"}')
    ws.send('{"type":"subscribe","symbol":"KUCOIN:ETH-USDT"}')


if __name__ == "__main__":
    
    print('Producer Start ...')
    
    websocket.enableTrace(False)
    while True:
        try:

            ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bpu4no7rh5red6hq49u0",
                                    on_message = on_message,
                                    on_error = on_error)
            ws.on_open = on_open
            ws.run_forever()
            
        except Exception as e:
            print(f"Connection lost: {e}. Reconnecting...")
            time.sleep(5)  # Wait for 5 seconds before attempting to reconnect

