#!/usr/bin/python

import os
import paramiko
import time
import re


#Variables that need to be set

hostname = 'remote.host'
port = 22
username = 'user'
dir_local = './var/log/apache/'
dir_remote = '/tmp/'
passwordFile = './secure/'

with open (passwordFile, "r") as myfile:
    password = myfile.read()
print password


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port,  username, password)

date = time.strftime("%Y_%m_%d_")
logList = [f for f in os.listdir(dir_local) if re.search(date+'(1[8-9]|2[0-1])\.log', f)]


sftp = ssh.open_sftp()
for log in logList:
        sftp.put(dir_local+log, dir_remote+log)

ssh.close()
