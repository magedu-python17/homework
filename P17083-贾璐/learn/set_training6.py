#!/usr/bin/env python

import random

list1 = []
list2 = []
flag = True
count = 0
while flag:
    list1.append(random.randrange(9,21))
    list2.append(random.randrange(9,21))
    count += 1
    if count == 10:
        flag = False
	
    
set1 = set(list1)
set2 = set(list2)
count1 = len(set1 | set2)
set3 = set1 ^ set2
set4 = set1 & set2
count2 = len(set3)
count3 = len(set4)
print(set1)
print(set2)
print("一共有{}个不同数字".format(count1))
print("两组元素中有{}个不重复的数字，它们是：{}".format(count2,set3))
print("两组元素中有{}个重复的数字，它们是：{}".format(count3,set4))
