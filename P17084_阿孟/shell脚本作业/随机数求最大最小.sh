#利用RANDOM生成10个随机数，并找出其中最大的值

#!/bin/bash
#
MAX=0
MIN=0
for I in {1..10};do
        DDD=$RANDOM
       [ $I -eq 1 ] && MIN=$DDD
        if [ $I -le 9 ];then
           echo -n "$DDD,"
        else
           echo "$DDD"
        fi
        [ $DDD -ge $MAX ] && MAX=$DDD
        [ $DDD -lt $MIN ] && MIN=$DDD
done

echo $MAX,$MIN