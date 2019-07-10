#!/usr/bin/env python
import re

ep = input("Enter a string:")


if re.search("1[0-9]{10}$",ep) != None:
    phone_number = re.search("1[0-9]{10}$",ep).group()
    print(phone_number)
elif re.search("0[0-9]{2,3}[\-0-9]{8}$",ep) != None:
    home_number = re.search("0[0-9]{2,3}[\-0-9]{8}$",ep).group()
    print(home_number)
else:
    print("There are no phone number in the string!")



