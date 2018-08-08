# --coding:utf-8--
import urllib2
import urllib
from sys import argv


url=argv[1]

request = urllib2.Request(url=url)
response = urllib2.urlopen(request)

print response.read()

