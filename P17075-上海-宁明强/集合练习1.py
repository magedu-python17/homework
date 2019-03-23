import random
lst1=[]
lst2=[]
for i in range(10):
    lst1.append(random.randint(10, 20))
    lst2.append(random.randint(10, 20))
a=set(lst1)
b=set(lst2)
print(a,b)
print(a.union(b))
print(a.symmetric_difference(b))
print(a.intersection(b))


