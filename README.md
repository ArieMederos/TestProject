

###Send logs to remote server####

The first python script "dailyLogs.py" search the logs from the current day (getting the 
date from the system) and send all the logs generated at the 18, 19, 20 and 21 hours
Following the format YYYY_MM_DD_HH.log
There are some variables that need to be set for the script to work, this was made on 
propuse to avoid hardcoded paths.



###Get the 500 errors###

The second python script "errors500.py" collect all the lines with 500 errors from the last 10 minutes.
Considering that this script behaves more like a manual tool, and not like a task that is needed 
to run on a schedule, the functionality of the script works giving the path to the log that need 
to be parsed through the command line
For example
python errors500.py /var/log/apache/2016_10_24_21.log
