import websocket
import json
import time
from datetime import datetime
from collections import ChainMap

fixedMinute = datetime.now().minute
averagePriceManager = ChainMap() 
prices = []
averagePriceManager[fixedMinute] = prices


def on_message(ws, message):
    global fixedMinute
    global averagePriceManager
    global prices
    json_dict = json.loads(message)
    currentMinute = datetime.now().minute
    currentDatetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price = json_dict.get('data')[0].get('p')
    volume = json_dict.get('data')[0].get('v') 
    print("{0} price:{1} volume:{2}".format (currentDatetime, price, volume))
     
    if currentMinute != fixedMinute:
        averagePriceManager[fixedMinute] = prices
        getAveragePricePerMinute(averagePriceManager)
        prices = []
        averagePriceManager[fixedMinute] = prices
        fixedMinute = currentMinute
    else:
        prices.append(float(price))

      
def getAveragePricePerMinute(averagePriceManager):
    sumOfPricesPerMinute = sum(averagePriceManager[fixedMinute])
    pricePositionsPerMinute = len(averagePriceManager[fixedMinute])
    print(sumOfPricesPerMinute/pricePositionsPerMinute)
    
    

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
    
     
    