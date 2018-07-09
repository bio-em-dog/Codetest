# --coding:utf-8--
import urllib
import urllib2

values = {"name":"13160827868","password":"jiaxudong225"}
values = {type=0&end_time=&track_count=10&page=1&user_id=47376}
data = urllib.urlencode(values)

url = "http://www.rabbitcycling.com/"
#url="http://www.rabbitcycling.com/v2/track/list?access_token=ZjIzZTQyZjA2MzFlNjY3YjI2NDcxMDI0OTM5ZDk4ZmE2ODliY2Q2NDk4YmIxYmQ0OTgxMmNkMDE1MzM1ZjFhMw"
#geturl = url + "?"+data

# headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"}
headers = {'Content-Type':'application/json'}
#request = urllib2.Request(geturl)
request = urllib2.Request(url=url,data=data,headers=headers)
response = urllib2.urlopen(request)

print response.read()
urllib2.Request()