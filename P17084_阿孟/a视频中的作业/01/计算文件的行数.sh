#04 练习：写一个脚本
#1、脚本可以接受一个以上的文件路径作为参数；
#2、显示每个文件所拥的行数；

#!/bin/bash
#
if [ $# -ge 1 ];then
        for i in $*;do #$*是将输入的所有参数转为列表
                wc -l $i|awk -F " " '{print $1}'
        done
else
        echo "pls input filepath"
fi