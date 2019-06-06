#!/usr/bin/env python

import shutil

src = "test"
dst = "test3"

with open(src) as f1:
    with open(dst,"w") as f2:
        shutil.copyfileobj(f1,f2)


