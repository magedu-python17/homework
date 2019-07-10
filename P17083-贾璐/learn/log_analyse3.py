#!/usr/bin/env python
import configparser
import json
ini_file = "ini_test.ini"
json_file = "json_test.json"
cfg = configparser.ConfigParser()
cfg.read(ini_file)
d = {}

for k,v in cfg.items():
    d[k] = dict(cfg.items(k))

with open(json_file,"w") as f:
    json.dump(d,f)
