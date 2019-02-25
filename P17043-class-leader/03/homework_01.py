# 将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式
# 单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",“1001”转化成为"壹仟零壹元"
# 数字的中文对应："零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"
# 请试着实验一下

# 这次的要求是代码尽量少
# 这次的要求是代码尽量少

lst_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_unit = ["零", "拾", "佰", "仟", "万"]
lst_word = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾"]
dict_transfer = dict(zip(lst_num,lst_word))
print("***数字转中文程序***")
while True:
    flag = False
    num = input('请输入数字 >>> ')
    if int(num) > 1:
        num = num.lstrip('0')
    if len(num) > 4:
        print('超出程序支持长度！！！')
        continue
    ret = []
    for x in num:
        ret.append(dict_transfer.get(int(x)))
    if len(num) == 5:
        ret.insert(1, "万")
        ret.insert(3, "仟")
        ret.insert(5, "佰")
        ret.insert(7, "拾")
    elif len(num) == 4:
        ret.insert(1, "仟")
        ret.insert(3, "佰")
        ret.insert(5, "拾")
        if ret[-3] == "零" and ret.count("零") < 3 and ret[-1] != "零":
            flag = True
        if "零" in ret:
            idx = ret.index("零")
            if idx == 2:
                ret.remove("佰")
                if "零" in ret:
                    idx = ret.index("零")
                    if idx == 2:
                        ret.remove("拾")
                        #print(ret)
                        if ret[-1] == ret[-2] and ret[-1] != "零":
                            ret.insert(-1, "拾")
                        #ret.remove("零")
                        if "零" in ret:
                            idx = ret.index("零")
                            if idx == 2:
                                ret.remove("零")
                                if "零" in ret:
                                    idx = ret.index("零")
                                    if idx == 2:
                                        ret.remove("零")
                                        if "零" in ret:
                                            idx = ret.index("零")
                                            if idx == 2:
                                                ret.remove("零")
            if idx == 4:
                ret.remove("拾")
                if "零" in ret:
                    idx = ret.index("零")
                    if idx == 4:
                        ret.remove("零")
                        if "零" in ret:
                            idx = ret.index("零")
                            if idx == 4:
                                ret.remove("零")
            if idx == 6:
                ret.remove("零")
        if flag is True:
            ret.insert(-1,"零")
        if ret[-1] == "零":
            ret[-1] = "拾"
        if ret[-1] == "拾" and ret[-3] == "仟" and len(ret) == 5:
            ret.insert(-2,"零")
        if ret[-2] == "拾" and len(ret) == 5 :
            ret.insert(2,"零")


    elif len(num) == 3:
        ret.insert(1, "佰")
        ret.insert(3, "拾")
        if ret[-3] == "零" and ret.count("零") == 1:
            flag = True
        if "零" in ret:
            idx = ret.index("零")
            if idx == 4:
                ret.remove("零")
            if idx == 2:
                ret.remove("零")
                ret.remove("拾")
                if "零" in ret:
                    idx = ret.index("零")
                    ret.remove("零")
        if flag is True:
            ret.insert(-1,"零")

    elif len(num) == 2:
        ret.insert(1, "拾")
        if "零" in ret:
            ret.remove("零")


    print( ''.join(ret) )

# 再想想有什么好的逻辑来实现妈？