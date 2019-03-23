#!/usr/bin/python

#print("This is my first python homework!")


def fuck(fn):
    print(f"fuck {fn.__name__[::-1].upper()}")

@fuck
def udiab():
    pass
