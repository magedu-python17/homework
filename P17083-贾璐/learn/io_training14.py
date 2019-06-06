#!/usr/bin/env python

from pathlib import Path

print(Path("/a/b/c/d/e.py").match("*.py"))
print(Path("/a/b/c/d/e.py").match("/a/*/*.py"))
print(Path("/a/b/c/d/e.py").match("/a/**/*.py"))
print(Path("/a/b/c/e.py").match("/a/**/*.py"))

f = Path("/home/python/python_project/3.5.3/homework/P17083-贾璐/learn/1.txt").open()
for i in f.readlines():
    print(i.strip())
f.close()


with Path("/home/python/python_project/3.5.3/homework/P17083-贾璐/learn/1.txt").open() as f:
    print(f.readline().strip())


print(Path("/home/python/python_project/3.5.3/homework/P17083-贾璐/learn/1.txt").read_text().strip())
