"""currencies development configuration."""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

DATA_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
    'data/'
)

CURRENCIES = ["CAD","HKD","ISK","PHP","DKK","HUF","CZK","GBP","RON","SEK","IDR",
"INR","BRL","RUB","HRK","JPY","THB","CHF","EUR","MYR","BGN","TRY","CNY","NOK",
"NZD","ZAR","USD","MXN","SGD","AUD","ILS","KRW","PLN"]