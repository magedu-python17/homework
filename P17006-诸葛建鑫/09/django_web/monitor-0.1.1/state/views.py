from django.shortcuts import render

# Create your views here.
from .models import AgentBase, AgentDisk, StateBase, StateDisk
from django.http import HttpRequest, HttpResponse, JsonResponse, QueryDict
from django.db.models import Q
import datetime
from collections import defaultdict
tz = 8
TZ = datetime.timezone(datetime.timedelta(hours=tz))


def state_show(request: HttpRequest, ip):
    query_req = request.GET
    item = query_req.getlist('item', ['cpu'])          # item允许的监控项为cpu, mem, disk
    print(query_req, item)
    if isinstance(item, list):
        keys = set(item)
        print('-----')
    else:
        keys = {item}
    print(keys)
    now = int(datetime.datetime.now(tz=TZ).timestamp())
    end = now - (now % 5 if now % 5 else 0)
    one_hour = end - 3600
    start, stop = one_hour, end
    interval = 40
    width = (stop - start) // interval
    date_list = [datetime.datetime.fromtimestamp(t, TZ).strftime('%H:%M:%S') for t in range(start, stop, width)]
    ret = {}
    qs = AgentBase.objects.values('id').filter(ip=ip).first()
    ab_id = qs['id']
    flag_cpu = True if 'cpu' in keys else False
    flag_mem = True if 'mem' in keys else False
    flag_disk = True if 'disk' in keys else False
    tmp = defaultdict(list)
    before = {}
    # print(start, stop)
    if flag_cpu or flag_mem:
        sbs = StateBase.objects.filter(agentbase_id=ab_id).order_by('date').filter(Q(date__gt=start) & Q(date__lt=stop)).all()
        sb_before = StateBase.objects.filter(agentbase_id=ab_id).order_by('-date').filter(date__lte=start).first()
        if sb_before:
            before['cpu'] = sb_before.cpu_percent
            before['mem'] = sb_before.memory_percent
        for sb in sbs:
            date = sb.date
            if flag_cpu:
                tmp['cpu'].append((date, sb.cpu_percent))
            if flag_mem:
                tmp['mem'].append((date, sb.memory_percent))
    if flag_disk:
        ads = AgentDisk.objects.filter(agentbase_id=ab_id).filter(is_deleted__isnull=True)
        lst = [ad.id for ad in ads]
        sds = StateDisk.objects.filter(agentdisk_id__in=lst).order_by('date')\
            .filter(Q(date__gt=start) & Q(date__lt=stop)).all()
        keys.remove('disk')
        for i in lst:
            sd_before = StateDisk.objects.filter(agentdisk_id=i).order_by('-date').filter(date__lte=start).first()
            if sd_before:
                dp = sd_before.agentdisk.dp
                before[dp] = sd_before.disk_percent
                keys.add(dp)
        for sd in sds:
            dp = sd.agentdisk.dp
            keys.add(dp)
            date = sd.date
            disk_percent = sd.disk_percent
            tmp[dp].append((date, disk_percent))
    # print('------------------', before, tmp, keys)
    for k in keys:
        data = tmp.get(k, [])
        bef = before.get(k, 0)
        ret[k] = time_width_max(bef, data, start, stop, width)
    ret['date'] = date_list
    print(ret)
    return JsonResponse(ret)


def extend(before, data: list, start, stop, interval):
    tim = range(start, stop, interval)
    if not data:            # 如果data为空，则说明时间段内无数据，使用上一次记录的时间
        ret = [before for _ in tim]
        return ret
    ret = []
    length = len(data)
    n = 0
    for t in tim:
        if n < length:
            if t < data[n][0]:
                before = before if before is not None else 0
                ret.append(before)
                continue
            else:
                before = data[n][1]
                if t == data[n][0]:
                    ret.append(before)
                n += 1
        else:
            ret.append(before)
    return ret


def time_width_max(before, data: list, start, stop, width):
    width = width if width >= 5 else 5
    tim = range(start, stop, width)
    if not data:
        ret = [before for _ in tim]
        return ret
    # st = sorted(data.keys())
    n = 0
    length = len(data)
    ret = []
    max_value = before if before else 0
    # print(data)
    for t in tim:
        if n < length:
            m = n
            while n < length and data[n][0] - t < width:
                if data[n][0] == t:
                    max_value = data[n][1]
                else:
                    max_value = max(max_value, data[n][1])
                n += 1
            else:
                ret.append(max_value)
                if m < n:
                    max_value = data[n-1][1]
        else:
            ret.append(max_value)
    return ret



# web 里面测试的话可以用print，不过最好建议要用logging 好点

# setting 里面 配置还不完善，等学完，回头再看看你的这个代码











