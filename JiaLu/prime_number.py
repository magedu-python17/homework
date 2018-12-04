#!/usr/bin/env python

num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a postive number!")
elif num <= 2:
    print("This number is prime number!")
else: 
    for i in range(3,num):
        if num % i == 0:
            print("This number is not prime number!")
            break
    else:
        print("This number is prime number!")
        
        
