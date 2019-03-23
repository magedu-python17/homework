import re

upper_regx = r'(?P<upper>[A-Z]+)'
lower_regx = r'(?P<lower>[a-z]+)'
int_regx = r'(?P<int>\d+)'
#regx = r'(?P<upper>[A-Z]+)?(?P<lower>[a-z]+)?(?P<int>\d+)?'

def filter(regx, s:str):
    new_string = ''
    pattern = re.compile(regx)
    for c in pattern.finditer(s):
        new_string += s[c.start():c.end()]
    return new_string

def rebuild_str(s:str):
    re_string = ''
    for regx in (upper_regx, lower_regx, int_regx):
        re_string += "".join(sorted(filter(regx, s)))
    print(re_string)

if __name__ == '__main__':
    s = input("pls input test_string>>>").strip()
    # test_string = "20WelcomeToMagEduSchool19"
    rebuild_str(s)

# 思路：
# 利用正则进行匹配分类进行迭代

# 第二周作业忘记写了，不好意思!
# 第三周作业暂时想不到迭代一遍，就将字符串归类好的方法，请小智老师提点