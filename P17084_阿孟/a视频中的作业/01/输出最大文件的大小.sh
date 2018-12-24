#传给脚本一个参数：目录，输出该目录中文件最大的，文件名和文件大小

#!/bin/bash
#
echo "`ls -l $1|grep "^-"|awk -F" " '{print $5}'`" > /test/list
i=0
while read line;do
        if [ $line -gt $i ];then
                i=$line
        #       echo "$i"
        fi
done < /test/list
MAX=$i
j=`ls -l $1|grep $MAX|awk -F" " '{print $9}'`
echo "MaxFileName:$j,FileSize=$MAX"