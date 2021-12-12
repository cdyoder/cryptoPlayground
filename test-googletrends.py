#! /home/chris/anaconda3/envs/crypto/bin/python

# code to get bitcoin prices from coinbase using coinbase-pro python library
# christopher d. yoder
# 09/12/2021
# 

# code to just run google trends file, debug and troubleshoot


import pdb
import numpy as np
import cbpro 
import os
import getpass
import datetime as dt
import googletrends as gt


# get trends
gt.GetTrends()
