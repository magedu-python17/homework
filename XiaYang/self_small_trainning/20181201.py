# 题目要求：
# 你得到一个可能混合大小写字母的字符串，你的任务是把该字符串转为仅使用小写字母或者大写字母，为了尽可能少的改变：
# 如果字符串包含的大字母数小于等于小写字母数，则把字符串转为小写。
# 如果大写的数目大于小写字母数，则把字符串转为全大写。
# 比如：
# solve('coDe')=="code"
# solve("CODe")=="CODE"

s = 'aABBssSSAAAAAAAjjjjjjjjj'
# 解法1
s_num = int(len(s))
s_lower = 0
s_upper = 0
for z in s:
    if z.islower():
        s_lower += 1
    else:
        s_upper += 1
if s_upper <= s_lower:
    print(s.lower())
else:
    print(s.upper())

# 解法2
lst_x = [x for x in s if x.islower()]
print(s.lower()) if len(s)//2 <= len(lst_x) else print(s.upper())
