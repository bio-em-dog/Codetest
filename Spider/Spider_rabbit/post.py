# --coding:utf-8--
import urllib
import urllib2

values = {
    "name": "13160827868",
    "password": "jiaxudong225"}
#'access_token': 'NTY5N2VkNmZiNDM5MjBjNzExYWM3ZjUzYzY3M2I4NTFlYWJjNThmNzhkYTFlZmFhNGY3YjEzOTcyMDI5YjkyYg'}

data = urllib.urlencode(values)

#url = "http://www.rabbitcycling.com/"
url = "http://www.rabbitcycling.com"
#    "?access_token=NTY5N2VkNmZiNDM5MjBjNzExYWM3ZjUzYzY3M2I4NTFlYWJjNThmNzhkYTFlZmFhNGY3YjEzOTcyMDI5YjkyYg"


# headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"}
#headers = {'Content-Type': 'application/json'}
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

print response.read()
