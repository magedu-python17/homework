#  新年新气象来份新的大作业精神一下，本周作业（1.2-1.13）  大作业两周布置一次哦 各位小伙伴们一定要提交时间很充足的
# 本周作业内容如下：
# # 知识点要求: 至少学到16节
# 第三次的作业：
#   s = "Sorting1234"
# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
# 1 所有的小写字母在大写字母前面
# 2 所有的字母在数字前面
# 3 所有的奇数在偶数前面

# 这次的要求是代码尽量少
# 这次的要求是代码尽量少

s = "Sorting1234"
print(''.join(sorted(s,key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper()))))

# 可以
