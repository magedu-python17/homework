num = int(input('》》'))
length = len(str(num))
if num < 100000 and num>=0:
    for x in range(length):
        tmp = num // 10
        print(num - ( tmp *10))
        num = tmp