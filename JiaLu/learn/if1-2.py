#!/usr/bin/python

def max_output(num1,num2):
    if num1 > num2:
        print("The Max num is %d" % num1)
    elif num1 < num2:
        print("The Max num is %d" % num2)
    else:
        print("num1 == num2!")

a=input("Enter two number: (num1 num2)")
num1 = int(a.split(" ")[0])
num2 = int(a.split(" ")[1])
max_output(num1,num2)
