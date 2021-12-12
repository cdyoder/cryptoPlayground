# code to play with monte carlos to buy and sell crypto
# Christopher D. Yoder
# 05-14-2021
# cd C:\Users\Christopher D. Yoder\Documents\crypto
#
# Problem Statement
# There is data for the following coins
#	Aave
#	BinanceCoin
#	Bitcoin
#	Cardano
#	ChainLink
#	Cosmos
#	CryptocomCoin
#	Dogecoin
#	EOS
#	Ethereum
#	Iota
#	Litecoin
#	Monero
#	NEM
#	Polkadot
#	Solana
#	Stellar
#	Tether
#	Tron
#	Uniswap
#	USDCoin
#	WrappedBitcoin
#	XRP
#
# Starting with $1000 and a nominal 2% fee whenever coin is sold/traded, find the best "winning" strategy
#	Defined as bank account value at the end of the period
#
# two pots of money:
#	in hand:	money in hand, not in the market
#	in coin:	sum of all coin balances
#
# prediction functions:
#	given history, predict the value of coin next time

# preamble
import numpy as np
import datetime as dt
import csv
import pdb
import os
import matplotlib.pyplot as plt

# define functions for use later
def BuySellHold(dates, coin_history, current_moneys, pen_rate):
	"""
	Function to choose to buy, sell, or hold for a given coin. 
	Assumes
		1. The last date in the vectors is the "today date" for use as current values
	INPUT
		dates 			= dates
		coin_history 	= data to date
		current_moneys 	= current value of [coins, in hand]
		pen_rate 		= penalty to move value of money around
	OUTPUT
		move_moneys 	= amount to buy, sell, 
	"""
	
	# get values 
	current_date = dates[len(dates) - 1]
	current_values = []
	
	# -------------------------------------------------------------
	# basic law: buy low sell high, hold otherwise
	
	
	# return things 
	return move_moneys

def FitFun():
	"""
	"""
	return 1

def ReadCoinIn(csvfile, datecol, **kwargs):
	"""
	Code to read in coin values from csv file. 
	INPUTS
		csvfile 		= coin sheet 
		datecol 		= date column
	OUTPUTS
		dates 			= datetime list of times
		coins 			= coin information in numpy list 
	KWARGS
		startdate 		= date to startdate
		enddate 		= date to end
	"""
	
	# handle kwargs
	startdate = dt.datetime(2000, 1, 1, 0, 0, 0)
	enddate = dt.datetime.today()
	if"startdate" in kwargs:
		startdate = kwargs["startdate"]
	if"enddate" in kwargs:
		enddate = kwargs["enddate"]
	
	# read in data first
	cntr = 0
	cntr2 = 0
	cntr3 = 0
	dates = []
	coins = np.empty((10000,10))
	with open(csvfile) as csvfid:
		csvdata = csv.reader(csvfile, delimiter=",")
		for row in csvfid:
			# skip header line
			# print(row)
			if cntr != 0:
				# get data out 
				c1 = row.split(',')
				rowdate = dt.datetime.fromisoformat(c1[datecol])
				cntr3 = len(c1) - datecol
				if rowdate >= startdate:
					if rowdate < enddate:
						# then record information
						dates.append(rowdate)
						cntr3 = len(c1) - datecol - 1
						# pdb.set_trace()
						for i1 in range(datecol + 1, len(c1)):
							coins[cntr2, i1 - datecol - 1] = float(c1[i1])
						cntr2 = cntr2 + 1
				# pdb.set_trace()
			cntr = cntr + 1
	
	# return things
	return dates, coins[0:cntr2, 0:cntr3]

def OrganizeData(datapairs, **kwargs):
	"""
	Code to get values at all date/time values for all coins
	INPUTS	
		datapairs 	= list of [datetime, datas] for all coins used
	OUTPUTS 
		
	"""
	
	return 1

def RunTime(runvec, ics_usd, datelist, coinlist, strategy, **kwargs):
	"""
	Code to iterate in time. 
	INPUTS	
		timevec 	= time to iterate over 
		ics 		= initial balances 
		datelist 	= coin dates
		coinlist 	= coin information at datelist points 
		strategy 	= 
	OUTPUTS	
		balances 	= USD balances of coins and in hand over runvec times AT THE END OF EVERY DAY
		coins 		= Coin balances of coins AT THE END OF EVERY DAY
	paradigm:
		move money, then simulate day motion of value
		assume that datelist is universal list of datetimes, coinlist is list of full coin informations
	"""
	
	# setup
	# coins = [coin1, coin2, ..., coinn, USD]
	balances = np.empty((len(runvec), len(ics)))
	currentbalance = np.copy(ics_usd)
	coins = np.empty((len(runvec), len(ics)))

	# initialize things
	moveperc = 0.25
	movefee = 0.025	# percent lost to coinbase
	moveusd = 2.50
	moveval_usd = 100	# usd to convert to coins
	
	# fast forward to runvec[0]
	cntr = 0
	currentcoin = 0*np.empty((len(ics), 1))
	for i1 in range(len(datelist)):
		# pdb.set_trace()
		if datelist[i1].date() == runvec[0].date():
			# if True:
			# pdb.set_trace()
			for j1 in range(len(ics)-1):
				currentcoin[j1] = USD2Coin(ics_usd[j1], coinlist[j1][i1, :], 0)
			currentcoin[j1+1] = ics_usd[j1+1]
			break
		cntr = cntr + 1
	ics_coin = np.copy(currentcoin)
	
	# run with choices
	usdloc = len(currentcoin)-1
	for i1 in range(len(runvec)):
		# choose strategy
		
		if strategy == "hodl":
			# HODL
			coinchange = 0*np.empty((len(ics)))
			
		elif strategy == "random":
			# strategy: pick value from [-1, 0, +1] for [sell, hodl, buy] for each coin
			coinchange = 0*np.empty((len(ics)))
			randv = []
			for k1 in range(len(ics)-1):
				# pick a value
				moveval = np.random.randint(low=-1, high=2)
				randv.append(moveval)
				if moveval == 1 and currentcoin[usdloc][0] > moveval_usd*(1 + movefee):
					# move from usd to coin
					# pdb.set_trace()
					coinchange[k1] = coinchange[k1] + USD2Coin(moveval_usd, coinlist[k1][i1, :], 0)
					coinchange[usdloc] = coinchange[usdloc] - moveval_usd*(1 + movefee)
				elif moveval == -1 and currentcoin[k1][0] > USD2Coin(moveval_usd, coinlist[k1][i1, :], 0):
					# move from coin to usd
					# pdb.set_trace()
					coinchange[k1] = coinchange[k1] - USD2Coin(moveval_usd, coinlist[k1][i1, :], 0)
					coinchange[usdloc] = coinchange[usdloc] + moveval_usd*(1 - movefee)
		
		elif strategy == "filter":
			# strategy: filter previous 30 days, make decision based on motion
			indxn = cntr - 30
			for k1 in range(len(ics)-1):
				y = coinlist[k1][indxn+i1:cntr+i1, 3]
				x = np.arange(0, len(y))
				z = np.polyfit(x, y, 5)
				p = np.poly1d(z)
				plt.plot(x, y, '.')
				plt.plot(x, p(x), '--')
				plt.show()
		
		# calculate value in USD
		for j1 in range(len(ics)-1):
			coins[i1, j1] = coinchange[j1] + currentcoin[j1]
			balances[i1, j1] = Coin2USD(coins[i1, j1], coinlist[j1][i1, :], 1)
			currentcoin[j1] = coins[i1, j1]
		coins[i1, j1+1] = coinchange[j1+1] + currentcoin[j1+1]
		balances[i1, j1+1] = coins[i1, j1+1]
		currentcoin[j1+1] = coins[i1, j1+1]
	
	# if nans
	if np.sum(np.isnan(balances)):
		pdb.set_trace()
	
	# all done, return things 
	return balances, coins	

def PlotResults_Single(datevec, balances, **kwargs):
	"""
	Code to plot the balances over time. 
	INPUTS	
		datevec 	= dates
		balances 	= [coins, in-hand]
	"""
	
	# make legend
	if "lgnd" in kwargs:
		lgnd = kwargs["lgnd"]
	else:
		lgnd = []
		for i1 in range(len(balances)-1):
			lgnd.append("Coin {0}".format(i1))
		lgnd.append("In-hand")
	
	# do the plots by day number
	dateno = np.arange(0, len(datevec), 1)
	for i1 in range(len(balances[0, :])):
		plt.plot(dateno, balances[:, i1], label=lgnd[i1])
		
	# sum and total balance
	curbal = np.copy(dateno)
	for i1 in range(len(dateno)):
		curbal[i1] = np.sum(balances[i1, :])
	plt.plot(dateno, curbal, label="Total")
	plt.xlabel('Day number')
	plt.ylabel('USD [$]')
	plt.grid(True)
	plt.legend()
	plt.show()

def PlotResults_Multi(datevec, balances, **kwargs):
	"""
	Code to plot the balances over time for several strategies. 
	INPUTS	
		datevec 	= dates
		balances 	= [coins, in-hand]
	"""
	
	# make legend
	if "lgnd" in kwargs:
		lgnd = kwargs["lgnd"]
	else:
		lgnd = []
		for i1 in range(len(balances)):
			lgnd.append("Strategy {0}".format(i1))
	
	# do the plots by day number
	dateno = np.arange(0, len(datevec), 1)
	for i1 in range(len(balances)):
		curbal = np.copy(dateno)
		for j1 in range(len(dateno)):
			curbal[j1] = np.sum(balances[i1][j1, :])
		plt.plot(dateno, curbal, label=lgnd[i1])	
	plt.xlabel('Day number')
	plt.ylabel('USD [$]')
	plt.grid(True)
	plt.legend()
	plt.show()

def USD2Coin(usd, coinLine, flag):
	"""
	Convert USD to number of coins. 
	INPUTS	
		usd			= amoutn of usd
		coinline 	= standard line of coin information
		flag 		= 0 if using open, 1 if using end
	OUTPUTS	
		coinnum 	= the equivalent amout of coin
	Assumes	
		coinLine: High,Low,Open,Close,Volume,Marketcap
	"""
	
	# convert
	return usd/float(coinLine[flag+2])

def Coin2USD(coin, coinLine, flag):
	"""
	Convert USD to number of coins. 
	INPUTS	
		coin		= amount of coin 
		coinline 	= standard line of coin information
		flag 		= 0 if using open, 1 if using end
	OUTPUTS	
		usdval  	= the equivalent amount of usd
	Assumes	
		coinLine: High,Low,Open,Close,Volume,Marketcap
	"""
	
	# convert
	return coin*float(coinLine[flag+2])




	

# main code
# ------------------------------------------------
# High, Low, Open, Close, Volume, Marketcap

# case 1: only bitcoin
csvlist = [os.path.join('archive', 'coin_Bitcoin.csv')]
datecol = [3]	# 3 = datetime information 
ics = [1000, 1000]	# bitcoin balance, in-hand balance
history_days = 30
startdate = dt.datetime(2017, 1, 1, 0, 0, 0)	# start date for analysis, lookback relative to this 
enddate = dt.datetime(2020, 1, 1, 0, 0, 0)		# end date



# read out datasets 
bigdates = []
biglists = []
for i1 in range(len(csvlist)):
	datelist, coinlist = ReadCoinIn(csvlist[i1], datecol[i1], startdate=startdate-dt.timedelta(days=history_days), enddate=enddate)
	bigdates.append(datelist)
	biglists.append(coinlist)
# pdb.set_trace()

# clean data for use

# run through time
runvec = datelist[history_days:len(datelist)]
balances_hodl, coins_hodl = RunTime(runvec, ics, datelist, biglists, "hodl")
# balances_rand, coins_rand = RunTime(runvec, ics, datelist, biglists, "random")
balances_rand, coins_rand = RunTime(runvec, ics, datelist, biglists, "filter")

# plots 
# PlotResults_Single(runvec, balances_hodl)		# plot single strategy in detail
PlotResults_Multi(runvec, [balances_hodl, balances_rand], lgnd=["Hodl", "Random"])
