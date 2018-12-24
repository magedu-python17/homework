#01 练习：写一个脚本
#1、创建目录/tmp/dir-当前日期时间；例如/tmp/dir-20150707-155503。
#2、在此目录中创建10个空文件，分别为file1-file10；

#!/bin/bash
#
mkdir -p /tmp/dir-`date +%F,%H:%M`
s="/tmp/dir-`date +%F,%H:%M`"
for i in {1..9};do
        mkdir -p $s/file$i
done