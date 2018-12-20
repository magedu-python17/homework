#03 练习：写一个脚本，完成以下任务。
#添加5个用户，user1-user5，每个用户的密码同用户名
#添加密码完成后不显示passwd执行结果
#显示添加成功信息

#!/bin/bash
#
for i in {1..5};do
        useradd user$i
        echo "user$i" | passwd --stdin user$i &>/dev/null
        echo "Add user$i access"
done