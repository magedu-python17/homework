from distutils.core import setup
import glob
setup(
    name="monitor",
    version="0.1.1",
    author="zhuge",
    author_email="zgjx1123@163.com",
    description="django jquery monitor",
    url="http://blog.luckysonia.com",
    packages=['monitor', 'state'],
    data_files=glob.glob('template/*.html')+['manage.py', 'requirement']+glob.glob('template/js/*.js')
)

