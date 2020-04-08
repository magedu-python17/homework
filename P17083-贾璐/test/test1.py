#!/usr/bin/env python
import re
str1 = 'Port-channel1.189         192.168.189.254    yes        CONFIG   up'
str_list = re.split(r'\s+',str1)
print(str_list)
