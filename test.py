# code to get bitcoin prices from coinbase using coinbase python library
# christopher d. yoder
# 09/12/2021

# conda activate crypto
# chdir Documents\crypto

import pdb
import numpy as np
from coinbase.wallet.client import Client

# create a client to get price data 
client = Client('api-key', 'api-secret')
# currency_code = 'USD'


# price = client.get_spot_price(currency_pair='BTC-USD', currency=currency_code)
price = client.get_spot_price(currency_pair='BTC-USD')
print(price.amount)
pdb.set_trace()
