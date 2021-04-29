import websocket
import json
import time
from datetime import datetime

fixedMinute = datetime.now().minute
averagePriceManager = {}
prices = []
volumes = []
averagePriceManager[fixedMinute] = prices


def on_message(ws, message):
    global fixedMinute
    global averagePriceManager
    global prices
    global volumes
    json_dict = json.loads(message)
    currentMinute = datetime.now().minute
    currentDatetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price = json_dict.get('data')[0].get('p')
    volume = json_dict.get('data')[0].get('v') 
    print("{0} price:{1} volume:{2}".format (currentDatetime, price, volume))
     
    if currentMinute != fixedMinute:
        averagePriceManager[fixedMinute] = prices
        getAveragePricePerMinute(averagePriceManager, volumes)
        prices = []
        volumes = []
        averagePriceManager[fixedMinute] = prices
        fixedMinute = currentMinute
    else:
        prices.append(float(price*volume))
        volumes.append(volume)

      
def getAveragePricePerMinute(averagePriceManager, volumes):
    sumOfPricesPerMinute = sum(averagePriceManager[fixedMinute])
    volumesPerMinute = sum(volumes)
    print(sumOfPricesPerMinute/volumesPerMinute)
    
    

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
    
     
    