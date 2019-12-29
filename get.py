import urllib.request, json 

#list of relavent currencies
currencies = ["CAD","HKD","ISK","PHP","DKK","HUF","CZK","GBP","RON","SEK","IDR",
"INR","BRL","RUB","HRK","JPY","THB","CHF","EUR","MYR","BGN","TRY","CNY","NOK",
"NZD","ZAR","USD","MXN","SGD","AUD","ILS","KRW","PLN"]

#recieves relavent list of currencies written in USD as a base
def getCurrencies(base='USD', print=False):
    get_url = "https://api.exchangeratesapi.io/latest?base=" + base
    out = "data/data_" + base + ".txt"
    with urllib.request.urlopen(get_url) as url:
        data = json.loads(url.read().decode())
        with open(out, 'w') as outfile:
            json.dump(data, outfile)
        if(print):
            readCurrencies(base)

#loads currency from data/data_base.txt and prints in easily readable tabular format
def readCurrencies(base='USD'):
    inFile = "data/data_" + base + ".txt"
    with open(inFile) as json_file:
        data = json.load(json_file)
        data = data['rates']
        for i in data:
            print(i + " " + str(data[i]))

for currency in currencies:
    getCurrencies(base=currency)