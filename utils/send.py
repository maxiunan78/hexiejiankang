#!/usr/bin/env python
#-*- coding:utf-8 -*-


 # -*- coding: utf-8 -*-
 #!/usr/bin/env python
import sys
import os
import json
import requests
sys.path.append(r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\User\insurance")


def senddatas(params):
	url = "http://dev-m.jhjbxj.com/api/product/queryProductPriceRate"
	# print params


	rowdata =  json.dumps(params)
	res = requests.post(url,{"productId":100008,"planId":100011,"propertyArray":rowdata})
	# res = requests.request('post',url=url,params=query)
	# print res.texts
	return  res
	# print type(res)
	# print json.loads(res.text)["body"]["payment"]

# if __name__ == '__main__':
# 	senddatas()