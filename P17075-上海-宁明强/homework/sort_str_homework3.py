s = "Sorting1234"
lowStr=[]
uppStr=[]
oddNum=[]
evnNum=[]
for i in s:
    if i.isalpha() and i.islower():
        lowStr.append(i)
    elif i.isupper():
        uppStr.append(i)
    if i.isdigit() and int(i)%2 == 0:
        evnNum.append(i)
    elif i.isdigit():
        oddNum.append(i)
print(''.join(sorted(oddNum)+sorted(evnNum)+sorted(lowStr)+sorted(uppStr)))

