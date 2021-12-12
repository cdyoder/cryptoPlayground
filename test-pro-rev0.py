#! /home/chris/anaconda3/envs/crypto/bin/python

# code to get bitcoin prices from coinbase using coinbase-pro python library
# christopher d. yoder
# 09/12/2021
# 

# conda activate crypto
# chdir Documents\crypto

# for install, had to pip install pymongo before pip install cbpro
# https://orangeable.com/server/linux-crontab
# https://stackoverflow.com/questions/36365801/run-a-crontab-job-using-an-anaconda-env

# goal: to tabulate the stats every day of various coins in USD for testing algorithms on later
#
# rev table
# rev0 
# rev1 	CDY 	11/03/2021 	Added month parsing to limit total file size


import pdb
import numpy as np
import cbpro 
import os
import getpass
import datetime as dt
import googletrends as gt

# list of coins - ranked by market quantity on 09-12-2021
# 01, Bitcoin, 868.7B
# 02, Ethereum, 401.4B
# --  03, Ethereum 2, 401.4B
# 04, Cardano, 83.0B
# --  05, Binance Coin, 70.2B
# 06, Tether, 68.3B
# --  07, XRP, 52.5B
# 08, Solana, 51.0B
# 09, Polkadot, 36.0B
# 10, Dogecoin, 33.0B
# --  11, USD Coin, 29.2B
# --  12, Terra, 15.9B
# 13, Uniswap, 14.6B
# 14, Chainlink, 13.3B
# --  15, Avalanche, 13.1B
# 16, Algorand, 12.8B
# --  17, Binance USD, 12.5B
# 18, Litecoin, 12.5B
# 19, Bitcoin Cash, 12.2B
# 20, InternetComputer, 9.7B
# 21, Wrapped Bitcoin, 9.4B
# --  22, FTX Token, 8.9B
# 23, Polygon, 8.9B
# 24, Filecoin, 8.8B
# --  25, TRON, 8.2B
# 26, Cosmos, 8.1B
# 27, Stellar Lumens, 7.9B
# --  28, VeChain, 7.7B
# 29, Ethereum Classic, 7.5B
# --  30, THETA, 6.6B
# 31, DAI, Dai, 6.6B
# 32, UST, TerraUSD, 2.5B
# 33, COMP, Compound, 5.5M
# 34, AMP, Amp, 42.2B
# 35, DASH, Dash, 10.3M
# 36, CHZ, Chiliz, 5.9B
# 37, ZEC, Zcash, 12.6M
# 38, CGLD, Celo, 306.8M
# 39, MANA, Decentraland, 1.8B
# 40, SUSHI, SushiSwap, 127.2M
# 41, ENJ, Enjin Coin, 834.3M
# 42, OMG, OMG Network, 140.2M
# 43, SNX, Synthetix Network Token, 114.8M
# 44, YFI, yerarn.finance, 36.6K
# 45, BAT, Basci Attention Token, 1.5B
coinlist = ['BTC', 'ETH', 'ETH2', 'ADA', \
	'USDT', 'XRP', 'SOL', 'DOT', \
	'DOGE', 'USDC', 'LUNA', 'UNI', 'LINK', \
	'ALGO', 'LTC', 'BCH', \
	'ICP', 'WBTC', 'FTT', 'MATIC', 'FIL', \
	'TRX', 'ATOM', 'XLM', 'VET', 'ETC', \
	'THETA', 'DAI', 'UST', 'COMP', 'AMP', \
	'DASH', 'CHZ', 'ZEC', 'CGLD', 'MANA', \
	'SUSHI', 'ENJ', 'OMG', 'SNX', 'YFI', \
	'BAT'] 			
	


# log file since cron doesn't seem to do it
coinlist.sort()
activity_log = os.path.join(os.getcwd(), 'test-pro-output.log')
if not os.path.join(activity_log):
	logfid = open(activity_log, 'w')
	logfid.write('test-pro.py logfile\n')
	logfid.close()


# directories
cryptodir = os.path.join(os.getcwd(), 'coin-bin')
if not os.path.exists(cryptodir):
	os.mkdir(cryptodir)

# files - preallocate and make
coinfilelist = []
for i1 in coinlist:
	coinname = os.path.join(cryptodir, i1.strip() + '.csv')
	coinfilelist.append(coinname)
	if not os.path.exists(coinname):
		# create files as needed
		fid = open(coinname, 'w')
		fid.write('Coin on file:\t' + i1 + '\n')
		fid.write('Created by:\t' + getpass.getuser() + '\n')
		fid.write('Created on:\t' + dt.datetime.utcnow().strftime("%m/%d/%YT%H:%M:%sZ") + '\n\n')
		fid.write('Recorded,Currency,Open,High,Low,Volume,Last,Volume30day\n')
		fid.close()


# create a client to get price data 
pc = cbpro.PublicClient()
moneytype = '-USD'


# get 24-hour stats
recordzulu = pc.get_time()['iso']
skipflag = 0
logfid = open(activity_log, 'a')
logfid.write(dt.datetime.utcnow().strftime("%m/%d/%YT%H:%M:%SZ") + '\n')
for i1 in coinlist:
	logfid.write(i1 + ',')
logfid.write('\n')
for i1 in range(len(coinlist)):
	# pdb.set_trace()
	try:
		a1 = pc.get_product_24hr_stats(coinlist[i1].strip() + moneytype)
		strline = "{0:20},{1:4},{2:010},{3:010},{4:010},{5:010},{6:010},{7:010}\n".format(recordzulu, moneytype, \
			float(a1['open']), float(a1['high']), float(a1['low']), float(a1['volume']), float(a1['last']), float(a1['volume_30day']))
		#strline = recordzulu + ',' + moneytype + ',' + a1['open'] + ',' + a1['high'] + ',' + a1['low'] + \
		#	',' + a1['volume'] + ',' + a1['last'] + ',' + a1['volume_30day'] + '\n'
		
		fid = open(coinfilelist[i1].strip(), 'a')
		fid.write(strline)
		fid.close()
		logfid.write('YES,')
		#print("#" + str(i1) + "\t" + coinlist[i1] + ":\t" + strline[0:len(strline)-2])
	except:
		#print("#--\t" + coinlist[i1] + ":\tNope...")
		skipflag += 1
		logfid.write('FAIL,')
logfid.write('\n')
logfid.close()

# get trends
gt.GetTrends()
