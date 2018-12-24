取本机IP地址？
a)ifconfig|ifconfig|sed -n '2p'|sed 's#^.*inet ##g'|sed 's#  net.*$##g'
b)ifconfig|sed -n '2p'|sed -r 's#^.*inet (.*)  net.*$#\1#g'
c)ifconfig|sed -nr '2s#^.*inet (.*)  net.*$#\1#gp'     ---此方法实际就是将b)方法后两个管道命令合并了
d)ifconfig|sed -n '2s#^.*inet \(.*\)  net.*$#\1#gp'
e)ifconfig|awk -F ' ' 'NR==2 {print $2}'
f)ifconfig|sed -n '2p'|awk -F ' ' '{print $2}'