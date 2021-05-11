import websocket
import json
from datetime import datetime

fixedMinute = datetime.now().strftime("%Y-%m-%d %H:%M")
trades_data = {}

def on_message(ws, message):
    global fixedMinute
    global trades_data
    json_dict = json.loads(message)
    time_of_deal = json_dict.get('data')[0].get('t')
    time_of_deal_converted = datetime.fromtimestamp(time_of_deal/1000)
    minute_of_deal = time_of_deal_converted.strftime('%Y-%m-%d %H:%M')
    string_time_of_deal = time_of_deal_converted.strftime('%Y-%m-%d %H:%M:%S')
    price = json_dict.get('data')[0].get('p')
    volume = json_dict.get('data')[0].get('v')
    average_price = price*volume/volume
    if minute_of_deal in trades_data:
        new_volume = trades_data[minute_of_deal][1] + volume
        new_average_price = trades_data[minute_of_deal][0] + average_price
        trades_data[minute_of_deal]=[new_average_price, new_volume]    
    else:
        trades_data[minute_of_deal]=[average_price, volume]
    print("{0} price:{1} volume:{2}".format(string_time_of_deal, price, volume))
    
     
    if minute_of_deal != fixedMinute:
        print(trades_data[fixedMinute][0])
        fixedMinute = minute_of_deal


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    data = ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')


if __name__ == "__main__": 
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c1hd51n48v6t9ghts9cg",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()     
    
     
    