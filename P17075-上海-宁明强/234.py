import random
lst='abcdefghijklmnopqrstuvwxyz'
for i in range(10):
    print('{:>04d}.{}'.format(i,''.join([lst[random.randint(0,25)] for j in range(10)])))