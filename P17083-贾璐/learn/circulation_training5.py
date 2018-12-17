#!/usr/bin/env python

score = int(input("Enter student's score: "))

if score > 100:
    print("Wrong score!")
elif score > 89:
    print("A")
elif score < 90 and score > 79:
    print("B")
elif score < 80 and score > 69:
    print("C")
elif score < 70 and score > 59:
    print("D")
elif score < 60 and score >= 0:
    print("E")
else:
    print("Wrong score!")
