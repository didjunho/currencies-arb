import urllib.request, json, threading
from datetime import datetime

# List of relavent currencies
currencies = ["CAD","HKD","ISK","PHP","DKK","HUF","CZK","GBP","RON","SEK","IDR",
"INR","BRL","RUB","HRK","JPY","THB","CHF","EUR","MYR","BGN","TRY","CNY","NOK",
"NZD","ZAR","USD","MXN","SGD","AUD","ILS","KRW","PLN"]

def getCurrencies(base='USD', printout=False):
    '''Recieves relavent list of currencies written in USD as a base.'''
    get_url = "https://api.exchangeratesapi.io/latest?base=" + base
    out = "../data/data_" + base + ".txt"
    with urllib.request.urlopen(get_url) as url:
        data = json.loads(url.read().decode())
        with open(out, 'w') as outfile:
            if base == 'EUR':
                data['rates']['EUR'] = 1
            json.dump(data['rates'], outfile)
        if(printout):
            readCurrencies(base)

def readCurrencies(base='USD'):
    '''Loads currency from data/data_base.txt and prints in easily readable tabular format.'''
    inFile = "../data/data_" + base + ".txt"
    with open(inFile) as json_file:
        data = json.load(json_file)
        data = data['rates']
        for i in data:
            print(i + " " + str(data[i]))

def startCurrencyThreads():
    '''Process each currency in a different thread.'''
    threads = []
    for currency in currencies:
        threads.append(threading.Thread(target=getCurrencies, args=(currency,)))
    now = datetime.now()
    # Month day, year H:M:S
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")
    out = "../data/data_time.txt"
    with open(out, 'w+') as outfile:
        outfile.write('{"time":"' + dt_string + '"}')
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

startCurrencyThreads()