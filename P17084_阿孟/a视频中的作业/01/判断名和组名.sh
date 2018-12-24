#06 练习:
#指定一个用户名,判断此用户的用户名和它的基本组的组名是否相同

#!/bin/bash
#
username=$1
groupname=`id -ng $1`
if [ $username == $groupname ];then
        echo yes
else
        echo no
fi