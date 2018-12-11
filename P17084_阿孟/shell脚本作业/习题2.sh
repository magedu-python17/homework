#02 练习：写一个脚本
#1、创建用户tuser1-tuser9; 
#2、创建目录/tmp/dir-当前日期；
#3、在/tmp/dir-当前日期 目录中创建9个空文件file101-file109
#4、将file101的属主改为tuser1，依次类推，一直将file109的属主改为tuser9;

#!/bin/bash
#
mkdir -p /tmp/dir-`date +%F,%H:%M`
s="/tmp/dir-`date +%F,%H:%M`"
for i in {1..9};do
        touch $s/file$i
        useradd tuser$i && chown tuser$i $s/file$i &>/dev/null
done