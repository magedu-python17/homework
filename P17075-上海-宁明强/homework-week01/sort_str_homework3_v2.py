s = "Sorting1234"
#print(ord(s[0]))
lowStr=[i for i in s if i.isalpha() and i.islower()]
uppStr=[i for i in s if i.isalpha() and i.isupper()]
evnNum=[i for i in s if i.isdigit() and int(i)%2 == 0]
oddNum=[i for i in s if i.isdigit() and int(i)%2 != 0]
print(''.join(sorted(oddNum)+sorted(evnNum)+sorted(lowStr)+sorted(uppStr)))