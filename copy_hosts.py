#!/usr/bin/env python
# coding:utf8

'''

function : copy hosts to local (centos7) with crontab to use
author   : Zhangze
date     : 2016-12-14

'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib
import datetime
import json
from bs4 import BeautifulSoup
from shutil import copyfile



request = urllib2.Request(url='https://raw.githubusercontent.com/racaljk/hosts/master/hosts')
response = urllib2.urlopen(request, timeout=20)
result = response.read()
result = BeautifulSoup(result)

content = result.get_text()

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
