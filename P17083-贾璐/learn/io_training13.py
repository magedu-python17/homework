#!/usr/bin/env python
from pathlib import Path
p = Path()
s = p.absolute()
print(str(s))
p1 = p /"a"/"b"/"c"/"d/e"/"f.py"
print(str(p1))
print(p1.absolute().parts)

path_parents = p1.parents

for i in path_parents:
    print(i)

print(path_parents[len(path_parents) - 1])

print(p1.name)
print(p1.home())
print(p1.suffix)
p3 = p1
print(p3.with_name("test"))
print(p3.with_suffix(".xml"))
print(p3.suffixes)
print(Path(str(p3) + ".xml").suffixes)


#  dir
p4 = Path(".")
print(p4.is_file())
print(p4.is_dir())
print(p4.cwd())
print(p4.home())
print(p4.is_absolute())
print(p4.exists())

s_dirs = s.parents[0].iterdir()
for i in s_dirs:
    print(i)

p5 = Path("/home")

for i in p5.rglob("func*"):
    print(i)
