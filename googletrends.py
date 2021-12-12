# code to test google trends 
# christopher d. yoder
# 09/17/2021
#
# rev0 - CDY - 09/17/2021 - initial revision
# rev1 - CDY - 09/23/2021 - modified read in of dictionary entries to handle ',' in gogle search terms
# rev2 - CDY - 11/03/2021 - modified to use different directories 

def GetTrends():
	# load things 
	from pytrends.request import TrendReq
	import pdb
	import os
	import getpass
	import datetime as dt
	# pdb.set_trace()
	
	nowdate = dt.datetime.now()
	yearmonth = nowdate.strftime("%Y-%m-")

	# preamble
	trendsdir = "trends"		# directory
	trendsfile = yearmonth + "trends.txt"	# trends recorded from google 
	trendsnum = 20			# number of trends to gather
	countryval = 'united_states'	# country of search
	searchval = 'trending'		# trending - type of search 
	dictfile = yearmonth + "word-to-num.txt"	# convert words to numbers 
	numsfile = yearmonth + "trends-num.txt"	# same as trends, just in numbers 
	indexfile = "number.txt"	# number of the trends to use

	# make full files 
	trendsfull = os.path.join(trendsdir, trendsfile)
	numberfull = os.path.join(trendsdir, numsfile)
	convertfull = os.path.join(trendsdir, dictfile)
	indexfull = os.path.join(trendsdir, indexfile)

	# check if files exist
	if os.path.exists(trendsdir) != 1:
		os.mkdir(trendsdir)
	if os.path.exists(trendsfull) != 1:
		fid = open(trendsfull, 'w')
		fid.write('Trends file:\n')
		fid.write('Created by:\t\t' + getpass.getuser() + '\n')
		fid.write('Created on:\\tt' + dt.datetime.utcnow().strftime("%m/%d/%YT%H:%M:%sZ") + '\n')
		fid.write('Number of trends:\t' + str(trendsnum) + '\n')
		fid.write('Country:\t\t{0}\n'.format(countryval))
		ttlstr = "Zulu,"
		for i1 in range(trendsnum):
			ttlstr = ttlstr + "#" + str(i1) + ","
		fid.write(ttlstr + '\n\n')
		fid.close()
	if os.path.exists(numberfull) != 1:
		fid = open(numberfull, 'w')
		fid.write('Number file:\n')
		fid.write('Created by:\t\t' + getpass.getuser() + '\n')
		fid.write('Created on:\t\t' + dt.datetime.utcnow().strftime("%m/%d/%YT%H:%M:%sZ") + '\n')
		fid.write('Number of trends:\t' + str(trendsnum) + '\n')
		fid.write('Country:\t\t{0}\n'.format(countryval))
		ttlstr = "Zulu,"
		for i1 in range(trendsnum):
			ttlstr = ttlstr + "#" + str(i1) + ","
		fid.write(ttlstr + '\n\n')
		fid.close()
	if os.path.exists(convertfull) != 1:
		fid = open(convertfull, 'w')
		fid.write("crypto,0\n")
		fid.close()
	if os.path.exists(indexfull) != 1:
		fid = open(indexfull, 'w')
		fid.write('0\n')
		fid.close()

	# load dictionary file for later
	converts = dict()
	fid = open(convertfull, 'r')
	newline = fid.readline()
	# pdb.set_trace()
	while newline:
		c1 = newline.strip().split(',')
		# rev0
		# converts[c1[0]] = int(c1[1])
		# rev1, issue with comma in search trends
		argn = int(c1[-1])
		argt = newline[0:newline.find(','+str(c1[-1]))]
		converts[argt] = argn
		newline = fid.readline()
	fid.close() 

	# load index for working
	fid = open(indexfull, 'r')
	indxval = int((fid.readline()).strip()) + 1
	fid.close()

	# make google object
	pytrend = TrendReq()

	# get daily search trends
	if searchval == 'trending':
		df = pytrend.trending_searches(pn=countryval)
		# print(df.items())

	# add to the dictionary
	linetime = dt.datetime.utcnow().strftime("%m/%d/%YT%H:%M:%sZ")
	fidtxt = open(trendsfull, 'a')
	fidnum = open(numberfull, 'a')
	ttlstr = linetime + ","
	numstr = linetime + ","
	for i1 in df.values:
		# add to the dictionary 
		if i1[0] not in converts:
			converts[i1[0]] = indxval
			indxval = indxval + 1
		# write it to the file for later use
		ttlstr = ttlstr + i1[0] + ","
		numstr = numstr + str(converts[i1[0]]) + ","
	fidtxt.write(ttlstr + "\n")
	fidtxt.close()
	fidnum.write(numstr + "\n")
	fidnum.close()

	# write to the dictionary file and index files
	fid = open(convertfull, 'w')
	for key in converts:
		fid.write("{0},{1}\n".format(key, converts[key]))
	fid.close()
	fid = open(indexfull, 'w')
	fid.write(str(indxval - 1) + "\n")
	fid.close()

if __name__ == "main":
	GetTrends()
