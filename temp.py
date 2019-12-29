import urllib.request, json 

#recieves relavent list of currencies written in USD as a base
def getCurrencies() :
    with urllib.request.urlopen("https://api.exchangeratesapi.io/latest?base=USD") as url:
        data = json.loads(url.read().decode())
        with open('data.txt', 'w') as outfile :
            json.dump(data, outfile)
        readCurrencies()

#loads currency from data.txt and prints in easily readable tabular format
def readCurrencies() :
    with open('data.txt') as json_file :
        data = json.load(json_file)
        data = data['rates']
        for i in data :
            print(i + " " + str(data[i]))

#getCurrencies()
readCurrencies()