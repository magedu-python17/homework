#   给定一个不超过5位的正整数，判断该数的位数，依次打印出十位，百位千位，万位的数字

num = int(input('》》'))
length = len(str(num))
if num < 100000 and num>=0:
    for x in range(length):
        tmp = num // 10
        print(num - ( tmp *10))
        num = tmp