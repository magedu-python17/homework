#!/usr/bin/env python
def nested_dict_builder(data, k, v):

    key_list = k.split('.')
    curr_data = data
    for i in key_list[:-1]:
        if i in curr_data.keys():
            curr_data = curr_data[i]

        else:
            curr_data[i] = {}
            curr_data = curr_data[i]

    curr_data[key_list[-1]] = v
res = dict()
d1 = {'A':1, 'B.A':2, 'B.B':3, 'CC.D.E':4, 'CC.D.F':5}
for k, v in d1.items():
    nested_dict_builder(res, k, v)

print(res)
