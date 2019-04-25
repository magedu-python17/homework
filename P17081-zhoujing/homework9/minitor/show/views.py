from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponse
from .models import Host, Disk, Cm_state, Disk_state
import math
from collections import defaultdict
# Create your views here.

def avalible(dict, method, key, default, func):
    try:
        ret = method(dict.get(key,default))
        ret = func(ret,default)
    except:
        ret = default

    return ret



def getall(request:HttpRequest):
    size = avalible(request.GET, int, 'size', 20, lambda x,y:x if x>0 and x< 40 else y)
    page = avalible(request.GET, int, 'page', 1, lambda x, y: x if x > 0 else y)
    start = (page -1) * size

    host = Host.objects.order_by('id')
    count = host.count()
    hosts = Host.objects.order_by('id')[start:start+size]
    return JsonResponse({'hosts':[
        {'id':host.id,'ip':host.ip} for host in hosts
    ],'pagination':{
        'page':page,
        'size':size,
        'pages':math.ceil(count/size),
        'count':count
    }
    })
def get(request:HttpRequest, id):
    id = int(id)
    host = Host.objects.get(pk=id)
    cm_states = Cm_state.objects.filter(host=host)
    disk_states = Disk_state.objects.filter(disk__host__id=id)
    state = defaultdict(list)
    for cm_state in cm_states:
        state['cpu_percent'].append(cm_state.cpu_percent)
        state['men_percent'].append(cm_state.men_percent)
        state['date'].append(cm_state.date)
    for disk_state in disk_states:
        state[disk_state.disk.partition].append(disk_state.size_percent)

    return JsonResponse({'state':
                             {'ip':host.ip,
                              'hostname':host.hostname,
                              'states':state
                              }})