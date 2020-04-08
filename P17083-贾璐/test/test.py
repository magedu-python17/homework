#!/usr/bin/env python
import re
str1 = 'Port-channel1.189         192.168.189.254    yes        CONFIG   up'
init_list = str1.split(' ')
str_list = list(set(init_list))
str_list.sort(key = init_list.index) 
print('-'*80)
print('接口     :',str_list[0])
print('ip地址      :',str_list[2])
print('状态      :',str_list[5])
