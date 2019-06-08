#!/usr/bin/env python



CHARS = set(""",.()[]-+/\*&%#$@`!'" \r\n\t""")

def _makekey2(key:str,chars=CHARS):
    start = 0
    for i,c in enumerate(key):
        if c in chars:         #如果字符属于CHARS字符集中的元素，那么就可以进行字符串切割
            if start == i:     #这里把特殊字符跳过
                start += 1
                continue
            yield key[start:i]  #切割字符串，将正常字符串放入yield中
            start = i + 1   #标记等于当前字符串（包含特殊字符）末尾加一
    else:                 #切到最后一个特殊字符以后，for循环就基本不会操作了，所以特殊字符后面的字符串需要通过else来补齐
        if start < len(key):    #判断最后一个特殊字符后面是否还有字符串
            yield key[start:]   #将最后的字符串全部放入yield！


def word_count(filename,encoding='utf-8',ignorewords=set()):
    d = {}
    with open(filename,encoding=encoding) as f:
        for line in f:
            for word in map(str.lower,_makekey2(line)):   #通过使用map函数将所有字符串变成小写
                if word not in ignorewords:   #根据忽略词汇的集合来判定哪些word忽略掉
                    d[word] = d.get(word,0) + 1   #dict的get方法是当word不在dict中的时候给他默认添加一个值为0，否则get这个key的值。
    return d


def top(d:dict,n:int=10):    #top迭代器，使用者可以根据自己需求来进行处理！
    for i,(k,v) in enumerate(sorted(d.items(),key=lambda item:item[1],reverse=True)): #对dict中的值进行反向排序，并把值的前十名抠出来。
        if i >= n:
            break
        yield (k,v)

for k,v in top(word_count('sample.txt',ignorewords={"the","a"})):   #忽略“the”和“a”这两个words！
    print(k,v)
