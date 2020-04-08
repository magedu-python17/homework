#!/usr/bin/env python

import re
import os,sys

dict1 = {}
vlan_list = []


with open('test.txt','r+') as f:
    lines = f.readlines()
for line in lines:
    if '-' in line:
        continue
    elif 'INCOMPLETE' in line:
        continue
    elif 'Vlan' in line:
        vlan_str = re.split('\s+',line)[3]
        if vlan_str in vlan_list:
            if dict1[vlan_str] >= 5:
                continue
            else:
                with open('test-new.txt','a+') as f:
                    f.write(line)
                dict1[vlan_str] += 1
        else:
            vlan_list.append(vlan_str)
            dict1[vlan_str] = 1
            with open('test-new.txt','a+') as f:
                f.write(line)


        



