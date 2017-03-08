# -*- coding:utf-8 -*-

import urllib2
import urllib
import json

#测试屏蔽新闻源是否生效
block_cpId=0
count=20
publisherId=[]
originurl="http://n.m.ksmobile.net/news/fresh?nmnc=01&scenario_param=&pid=14&lon=0.0&mcc=460&preload=0&declared_lan=en_US&mode=2&osv=6.0&act=3&regionid=1&scenario=0x001d0101&appv=7.1.4&lan=en_US&action=0xe72ef&model=HTC_M9u&net=wifi&brand=htc&lat=0.0&newuser=0&mnc=01&offset=&ch=200000&ch_preinstall=htc&server_city=&display=0xeE1f8f&user_city=&nmcc=460&media_info=tw%2Cig%2Ctw2%2Cig2%2Cgif2&ctype=0x91a67&pf=android&v=5&aid=1fdea233f13f120"
url=originurl+"&"+"count="+str(count)
print url
req=urllib2.Request(url)
res_info=urllib2.urlopen(req).read()
res_js=json.loads(res_info)
data_info=res_js["data"]
for i in data_info:
    id=int(i["publisher_info"]["id"])
    publisherId.append(id)
    if(id==block_cpId):
        print "未屏蔽此新闻源的id为："+str(i["contentid"])

print publisherId





