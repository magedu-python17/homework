from setuptools import setup, find_packages
import glob
setup(
    name="myblog",
    version="0.1.1",
    author="zhuge",
    author_email="zgjx1123@163.com",
    description="uWSGI Django blog",
    url="http://blog.luckysonia.cn",
    packages=find_packages(exclude=('migrations/.*',)),
    data_files=glob.glob('static/**', recursive=True)+glob.glob(
        'templates/*.html')+['manage.py', 'requirement', 'simsun.ttc']
)


# a = glob.glob('static/**', recursive=True)
# print(len(a))
#
# from pathlib import Path
# import os
#
#
# def list_file(filepath, recursive):
#     ret = []
#
#     def _list_file(fp):
#         p = Path(fp)
#         if p.exists():
#             if p.is_dir():
#                 ret.append("{}{}".format(str(p), os.path.sep))
#                 if recursive:
#                     for sfp in p.iterdir():
#                         _list_file(sfp)
#             elif p.is_file():
#                 ret.append(str(p))
#     _list_file(filepath)
#     return ret
#
#
# lst = list_file('static', recursive=True)
# print(len(lst), lst)
# lst2 = list_file('web', recursive=True)
# print(len(lst2), lst2)












