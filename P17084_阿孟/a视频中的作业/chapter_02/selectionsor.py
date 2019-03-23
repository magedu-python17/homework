#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-12 15:55
#
# Filename: selectionsor.py
#
# Description: V1.0
#
#========================================================
lst = [5,6,2,9,1,3,0,7]
lenth = len(lst)
for i in range(lenth):
    maxindex = i
    for j in range(i+1,lenth):
        if lst[maxindex] > lst[j]:
            maxindex = j
    if maxindex != i:
        lst[maxindex],lst[i] = lst[i],lst[maxindex]
print(lst)
