#12、计算100以内所有能被3整除的整数的和

#b=$(($i%3))
#!/bin/bash
#
j=0
for i in {1..100};do
        if [ "$(($i%3))" -eq 0 ];then
                j=$((i+j))
        fi
done
echo "$j"