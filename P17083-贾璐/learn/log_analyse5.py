#!/usr/bin/env python
import argparse
from pathlib import Path
parser = argparse.ArgumentParser('ls',description="list directory contents",add_help=True)
parser.add_argument('path',nargs='?',default='.',help="help path arg")
parser.add_argument('-l',action='store_true')
parser.add_argument('-a','--all',action='store_true')

#args = parser.parse_args('-la'.split())
args = parser.parse_args()
print(args)


p = Path(args.path)
print(p)

