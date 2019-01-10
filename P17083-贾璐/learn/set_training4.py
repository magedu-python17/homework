#!/usr/bin/env python

api = {"A","B","C"}

user = {"B","C","D"}

if api.isdisjoint(user):
    print("你没有权限访问API")
else:
    print("你有权访问API")
