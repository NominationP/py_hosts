#!/usr/bin/env python
# coding:utf8

'''

function : copy hosts to local (centos7) with crontab to use
author   : Zhangze
date     : 2016-12-14

'''
import urllib.request
import datetime
fp = urllib.request.urlopen("https://raw.githubusercontent.com/racaljk/hosts/master/hosts")


mybytes = fp.read()

content = mybytes.decode("utf8")
fp.close()

# dup
fw = open('/var/www/html/py_hosts/hosts_new','w')
fw.write(content)
fw.close()

# local hosts
# need to input : "chmod 777 /etc/hosts" (not good)
fw = open('/etc/hosts','w')
fw.write(content)
fw.close()

# log ---> crontab
# time ---> crontab



print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
