#! /home/chris/anaconda3/envs/crypto/bin/python

import pdb
import datetime as dt

filename = "/home/chris/crypto/test-v2.log"
fid = open(filename, 'a')
fid.write("Test date:\t" + dt.datetime.utcnow().strftime("%m/%d/%YT%H:%M:%SZ") + " - this is hard...\n")
fid.close()

# print to file for later?
print(dt.datetime.utcnow().strftime("%m/%d/%YT%H:%M:%SZ"))

