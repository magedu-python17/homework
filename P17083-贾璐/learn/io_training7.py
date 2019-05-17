#!/usr/bin/env python


def copy_file(src,dst):
    with open(src) as f1:
        with open(dst,"w+") as f2:
            f2.write(f1.read())


copy_file("test","test1")
