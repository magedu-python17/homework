lower_case = []
capital = []
even_number = []
odd_number = []
new_str = input("请输入一个包含大小写字母,数字的字符串: ")
for i in new_str:
    if i.islower():
        lower_case.append(i)
    if i.isupper():
        capital.append(i)
    if i.isdigit() and int(i) % 2 == 0:
        even_number.append(i)
    if i.isdigit() and int(i) % 2 != 0:
        odd_number.append(i)
        
print("".join(sorted(lower_case))+"".join(sorted(capital))+"".join(sorted(odd_number))+"".join(sorted(even_number)))