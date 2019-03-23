#!/usr/bin/env python

def add_ellipsis1(input_type,comments):
    if input_type == list:
        for i in comments:
            if type(i) != str:
                i = str(i)
            if len(i) > 7:
                print(i[:7] + "...")
            else:
                print(i)
    elif input_type == tuple:
        for i in comments:
            if type(i) != str:
                i = str(i)
            if len(i) > 7:
                print(i[:7] + "...")
            else:
                print(i)
    else:
        print("wrong input type!")

def add_ellipsis(length,comments):
    return (str(x) if len(str(x)) < length else str(x)[:length] + "..." for x in comments)

#comments = ("Implementation note",
#            "Changed",
#            "ABC for generator")
comments = (123432543,321321321,432543543543,12345)
#input_type = type(comments)

length = int(input("Enter a length: "))
print("\n".join(list(add_ellipsis(length,comments))))

# 独秀的逻辑上没有问题