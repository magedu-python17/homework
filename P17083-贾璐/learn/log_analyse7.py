#!/usr/bin/env python
import re
import datetime
line = '''192.168.10.1 - - [10/Jul/2019:16:52:34 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''


ops = {'datetime':lambda timestr:datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M:%S %z'),'status': int, 'length':int}




def re_compile(pattern):
    regex = re.compile(pattern)
    return regex

def extract(line:str,regex,ops) -> dict:
    matcher = regex.match(line)
    if matcher:
        return {k:ops.get(k, lambda x:x)(v) for k,v in matcher.groupdict().items()}
    else:
        raise Exception("No match!")


pattern = '''(?P<remote_ip>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] \
"(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/\d.]+)" (?P<status>\d+) (?P<length>\d+) .+ "(?P<useragent>.+)"'''



regex = re_compile(pattern)

#print(regex.match(line))
print(extract(line,regex,ops))

