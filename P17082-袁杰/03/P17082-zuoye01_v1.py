#  s = "Sorting1234"
# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
# 1 所有的小写字母在大写字母前面
# 2 所有的字母在数字前面
# 3 所有的奇数在偶数前面

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

lower_case.sort()
capital.sort()
even_number.sort(key=int)
odd_number.sort(key=int)

print("".join(lower_case)+"".join(capital)+"".join(odd_number)+"".join(even_number))

# 提示下，想想元组的排序