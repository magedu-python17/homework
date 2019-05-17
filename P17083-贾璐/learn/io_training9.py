#!/usr/bin/env python



chars = set(r""",.()[]-+/\*&%#$@`""")

def makekey(x):
    key = x.lower()
    ret = []
    for c in key:
        if c in chars:
            ret.append(' ')
        else:
            ret.append(c)
    return "".join(ret).split()



encoding = 'utf-8'
d = {}

with open("sample.txt",encoding=encoding) as f:
    for line in f:
        words = line.split()
        for wordlist in map(makekey,words):
            for word in wordlist:
                d[word] = d.get(word,0) + 1


print(sorted(d.items(),keys=lambda item:item[1],reverse=True))


for k in d:
    if k.find('path') > -1:
        print(k)
