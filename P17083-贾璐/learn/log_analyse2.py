#!/usr/bin/env python
import configparser
import json
ini_file = "ini_test.ini"
json_file = "json_test.json"
ini2json_dict = {}
cfg = configparser.ConfigParser()
cfg.read(ini_file)
items = cfg.items()
for k,v in items:
    if k == "DEFAULT":
        ini2json_dict[k] = dict()
        option_vals = cfg.items(k)
        for option_val in option_vals:
            option,val = option_val
            ini2json_dict[k][option] = val
sections = cfg.sections()
for section in sections:
    ini2json_dict[section] = dict()
    options = cfg.options(section)
    for option in options:
        val = cfg.get(section,option)
        ini2json_dict[section][option] = val

with open(json_file,'w') as f:
    json.dump(ini2json_dict,f)


