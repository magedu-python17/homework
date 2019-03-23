#!/use/bin/env python


count = 0
for num in range(1,100000,2):
    if num ==0 or num == 1:
        continue
    elif num == 3:
        print("2 %d" % (num),end=" ")
        count += 1
    else: 
        if num % 2 == 0:
            continue
        else:
            for i in range(3,num,2):
                if num % i == 0:
                    break
            else:
                print(num,end=" ")
                count += 1
count += 1
print("\n")
print("%d\n" % count)
