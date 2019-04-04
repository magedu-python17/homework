#!/usr/bin/env python

def cmd_dispatcher():
    cmds = {}
    def reg(cmd):
        def _reg(fn):
            cmds[cmd] = fn
            return fn
        return _reg

    def dispatcher():
        def default_func():
            print("This is default function!")
    
        while True:
            cmd = input(">>>")
            if cmd == "quick":
                break
            cmds.get(cmd,default_func)()
    return reg,dispatcher

reg,dispatcher = cmd_dispatcher()
@reg('mag')
def mag():
    print("magedu")
@reg('py')
def py():
    print("python")


dispatcher()
