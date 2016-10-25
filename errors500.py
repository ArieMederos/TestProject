#!/usr/bin/python


import datetime
import re
import sys


parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
queryResult = []



if len(sys.argv)<2:
        print "You must specify a log file"
else:
	logFile = sys.argv[1]
     	with open(logFile) as f:
                lines = f.read().splitlines()
        for line in lines:
		if line:
	                m = pattern.match(line)
	                res = m.groupdict()
	                logT = datetime.datetime.strptime(res["time"][:-6], "%d/%b/%Y:%H:%M:%S")
	                if (datetime.datetime.now() - logT)<datetime.timedelta(minutes=10) and res['status'] == '500':
	                        queryResult.append(line)

if queryResult:
	for line in queryResult:
		print line
else:
	print "No results found"
