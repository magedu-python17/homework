#!/usr/bin/env python

from io import StringIO,BytesIO




with BytesIO() as sio:
    print(sio.readable(),sio.writable(),sio.seekable())
    sio.write(b"Hello Python!")
    print(1,sio.getvalue())

