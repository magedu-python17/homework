#!/usr/bin/env python


def add(x:int,y:int) -> int:
    """
        :param x: int
        :param y: int
        :return:  int
    """
    if add.__annotations__['x'] == type(x) and add.__annotations__['y'] == type(y):
        return x+y
    else:
        print("Wrong type:")
        return type(x),type(y)
print(add(4,5))
print(add('test','test'))
