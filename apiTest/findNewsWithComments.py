# -*- coding:utf-8 -*-
import urllib2
import urllib
import json

count=10
newsIdList=[]
num=50
originurl="http://n.m.ksmobile.net/news/fresh?nmnc=01&scenario_param=&pid=14&lon=0.0&mcc=460&preload=0&declared_lan=en_US&mode=2&osv=6.0&act=3&regionid=1&scenario=0x001d0101&appv=7.1.4&lan=en_US&action=0xe72ef&model=HTC_M9u&net=wifi&brand=htc&lat=0.0&newuser=0&mnc=01&offset=&ch=200000&ch_preinstall=htc&server_city=&display=0xeE1f8f&user_city=&nmcc=460&media_info=tw%2Cig%2Ctw2%2Cig2%2Cgif2&ctype=0x91a67&pf=android&v=5&aid=1fdea233f13f120"
url=originurl+"&"+"count="+str(count)

req=urllib2.Request(url)
rsp_info=urllib2.urlopen(req).read()
rsp=json.loads(rsp_info)
data=rsp["data"]

for i in data:
    print i["commentcount"]
    if int(i["commentcount"])>=50:
        newsIdList.append(i["contentid"])

print newsIdList