#!/usr/bin/env python

from inspect import signature

def add(x:int,y:int,*args,**kwargs):
    return x+y


sig = signature(add)

for i,item in enumerate(sig.parameters.items()):
    name,param = item
    print(i+1,name,param.annotation,param.kind,param.default)
    print(param.default is param.empty,end='\n\n')


