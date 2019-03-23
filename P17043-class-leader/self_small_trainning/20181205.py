import random

a = [1,2,3,4]
def generate(a):
    new_lst = []
    for _ in range(1000):
        x = random.randint(1,4)
        if x not in new_lst:
            new_lst.append(x)
    return new_lst
new_a = []
for _ in range(1000):
    xx = generate(a)
    if xx not in new_a:
        new_a.append(xx)
print(len(new_a))




from itertools import permutations


print(len(list(permutations([1,2,3,4,5,6]))))




