# --coding:utf-8--
import urllib2
import urllib

url = 'http://www.rabbitcycling.com/?username=13160827868&password=jiaxudong225'

values = {'name': '13160827868', 'password': 'jiaxudong225'}
data = urllib.urlencode(values)
page='type=0&end_time=&track_count=10&page=1&user_id=47376'
geturl = url + "?"+data+'&'+page+"#/ucenter"

print data
print geturl

request = urllib2.Request(url=geturl)
response = urllib2.urlopen(request)

print response.read()

"""
values = {
    "name": "13160827868",
    "password": "jiaxudong225",
    'access_token': 'NTY5N2VkNmZiNDM5MjBjNzExYWM3ZjUzYzY3M2I4NTFlYWJjNThmNzhkYTFlZmFhNGY3YjEzOTcyMDI5YjkyYg'}

data = urllib.urlencode(values)

url = "http://www.rabbitcycling.com"

headers = {
    'Content-Type': 'application/json',
    'Host': 'www.rabbitcycling.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.rabbitcycling.com/',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'biketo-version': '1.0',
    'biketo-channel': 'web',
    'origin': 'http://www.rabbitcycling.com',
    'Content-Length': '42',
    'Connection': 'keep-alive'}

request = urllib2.Request(url=url, data=data, headers=headers)
response = urllib2.urlopen(request)
"""