#coding=utf-8
#练习:依次接收用户输入3个数,排序后打印#
# 2.使用max函数
nums=[]
out=None
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
while True:
    cur=min(nums)
    print(cur)
    nums.remove(cur)
    if len(nums)==1:
        print(nums[0])
        break
