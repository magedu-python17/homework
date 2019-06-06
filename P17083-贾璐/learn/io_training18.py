#!/usr/bin/env python

import configparser

ini_file_name = "ini_test.ini"
cfg = configparser.ConfigParser()
cfg.read(ini_file_name)
cfg["mysql"]["value"] = str(400)

cfg.add_section("mysql_test")

with open("mysql.ini","w") as f:
    cfg.write(f)


