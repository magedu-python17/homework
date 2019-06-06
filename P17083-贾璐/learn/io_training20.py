#!/usr/bin/env python
import json

d = dict(zip("abcde",[None,True,False,[1,"abc"],{'a':1,'b':2}]))

print(json.dumps(d))
