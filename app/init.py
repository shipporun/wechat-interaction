# -*- coding:utf8 -*-
import time
import hashlib
import xml.etree.ElementTree as ET
from flask import Flask
from flask import request
from flask import make_response
from forcast import fetchWeather, sortData

app = Flask(__name__)
listH = []

@app.route('/', methods=['POST', 'GET'])
def wechat():
	if request.method == 'GET':
		if len(request.args) > 3:
			echostr = request.args['echostr']	#
			return echostr
		else:
			return 'Wanna get something?'
	else:
		i = ET.fromstring(request.data)		#
		server = i.find('ToUserName').text
		user = i.find('FromUserName').text
		msgtype = i.find('MsgType').text
		content = i.find('Content').text
		reply = '<xml><ToUserName><![CDATA[%s]]></ToUserName> \
			<FromUserName><![CDATA[%s]]></FromUserName> \
			<CreateTime>%s</CreateTime> \
			<MsgType><![CDATA[text]]></MsgType> \
			<Content><![CDATA[%s]]></Content> \
			<FuncFlag>0</FuncFlag></xml>'  #
		if msgtype == 'text':
			if content == 'help':
				content = '输入 城市名，获取当前天气 \
						输入 history，获取查询记录\
						输入 help，获取帮助文档'
			elif content == 'history':
				content = set(listH)
			else:
				data = fetchWeather(content, 1)
				if 'status' in data:
					content = 'No result. Need help?'
				else:
					a = sortData(data, key, 1)
					content = a[0]
					listH.append(a[0])
			o = make_response(reply % (user, server, str(int(time.time())), content))		
			o.content_type = 'application/xml'   #
			return o
		else:
			return 'success'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80) 
