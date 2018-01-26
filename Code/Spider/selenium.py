# --coding:utf-8--
import urllib2
import urllib
from selenium import webdriver

url = 'http://www.rabbitcycling.com/?username=13160827868&password=jiaxudong225'

browser = webdriver.Firefox()
browser.get(url)

