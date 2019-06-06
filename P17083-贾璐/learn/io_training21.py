#!/usr/bin/env python
import json
import msgpack

d = dict(zip("abcde",[None,True,False,[1,"abc"],{'a':1,'b':2}]))

print(len(json.dumps(d)))


print(len(msgpack.packb(d)))

b1 = msgpack.packb(d)
b2 = msgpack.unpackb(b1)
print(msgpack.unpackb(b1))
