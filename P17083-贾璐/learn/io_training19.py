#!/usr/bin/env python

import pickle

filename = "pickle_test"

d = {"a":1,"b":"abc","c":[1,2,3]}
l = list("123")
i = 99

n = pickle.dumps(d)
print(pickle.loads(n))
n = pickle.dumps(l)
print(pickle.loads(n))
n = pickle.dumps(i)
print(pickle.loads(n))


