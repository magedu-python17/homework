lst = []
lst1 = []
lst2 = []
lst3 = []
lst4 = []
while True:
    #包含大写英文字母、数字
    s = input("please input your string:")
    for i in range(len(s)):
        if s[i].isupper(): #大写字母
            lst1.append(i)
        elif s[i].islower(): #小写字母
            lst2.append(i)
        elif s[i].isdigit(): #数字
            if int(s[i]) % 2 != 0:
                lst3.append(i)  #奇数
            else:
                lst4.append(i)  #偶数
        else:
            print("存在非法字符，请重新输入!")
            break
    else:
        break
for j in range(len(lst2)):
    lst.append((0,s[lst2[j]]))
for k in range(len(lst1)):
    lst.append((1,s[lst1[k]]))
for m in range(len(lst3)):
    lst.append((2,s[lst3[m]]))
for n in range(len(lst4)):
    lst.append((3,s[lst4[n]]))
lst5 = sorted(lst)
for q in range(len(lst5)):
    print(lst5[q][1],end='',sep='')