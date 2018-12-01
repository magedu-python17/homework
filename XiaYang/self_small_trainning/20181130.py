# num_dict = {
#     '0':0,
#     '1':1,
#     '2':2,
#     '3':3,
#     '4':4,
#     '5':5,
#     '6':6,
#     '7':7,
#     '8':8,
#     '9':9
# }
# s = '123456789'
# i = 0
# for x in s:
#     i = i*10 + num_dict[x]
# print(i,type(i))


a = ['个','十','百','千','万','十万','百万','千万','亿']
new_dict = dict(enumerate(a,1))
print(new_dict)
i = 123456789
tmp = i
count = 0
while tmp > 10:
    tmp //= 10
    count += 1
num_count = count + 1

print('first num: {}{}, number count: {}'.format(tmp,new_dict.get(num_count),num_count))


