n = input('请输入一串只包含大小写字母和数字的字符串')
lowercase = [i for i in n if i.islower()]
capital = [i for i in n if i.isupper()]
oddnumber = [i for i in n if i.isdigit() and int(i) % 2 == 1]
evennumber = [i for i in n if i.isdigit() and int(i) % 2 == 0]
print(''.join(lowercase) + ''.join(capital) + ''.join(oddnumber) + ''.join(evennumber))

#代码写的蛮不错的，把排序的功能实现就非常完美
