from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse

import psutil
import datetime
import time
import getpass



# Create your views here.

def index(request):
    # 获取当前登录的用户名
    user = getpass.getuser()

    # 查看内存相关信
    mem = psutil.virtual_memory()

    return render(request,'index.html',{'cpu':int(psutil.cpu_percent(1)),
                     'men':int(mem.used/mem.total*100),'disk_C':int(psutil.disk_usage('C:\\').percent),
                    'disk_D':int(psutil.disk_usage('D:\\').percent),'disk_E':int(psutil.disk_usage('E:\\').percent),
                    'disk_F':int(psutil.disk_usage('F:\\').percent)
                                        })














