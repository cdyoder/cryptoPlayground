Data set taken from: https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory

Things to do:
1. Read in plots of crypto, see if they make sense
2. setup neural net to track datasets
3. 


# things install notes - crontab
crontab -e
m h d m y arg1

SHELL=/bin/bash forces cron to use bash instead of shell sh
*/1 * * * * arg1 runs arg1 every minute
* * * * * cd <dir> && python3 <pyfile> >> <logfile> changes the directory and then runs the script using python, logs things to the log file


working now, have to
set bash
set path 
***** cd <path/to/bin/> && cd <dir> && source activate <condaenv> && python <script.py> && source deactivate


