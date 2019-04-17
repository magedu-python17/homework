a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z','Y']
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c = '2131YbSeaYZwed4676797123'
lst1 = []
indexnum = []
indexnum2 = []
indexnum3 = []
indexnum4 = []
indexnum5 = []
for i in c:
   lst1.append(i)
for j in lst1:
   if j in b:
      indexnum.append(j)
   if j in a:
      indexnum2.append(j)
   if j not in a:
      if j not in b:
         indexnum3.append(j)
for i in indexnum3:
   if int(i) % 2 == 0:
      indexnum4.append(i)
   else:
      indexnum5.append(i)

newlst = indexnum + indexnum2 + indexnum4 + indexnum5
newstr = ''.join(newlst)
print(newstr)

#想到的这个笨方法，后续想到其他方法再写。