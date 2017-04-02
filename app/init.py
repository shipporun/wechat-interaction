# -*- coding:utf8 -*-
import time
from flask import Flask
from flask import request
from flask import make_response
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)

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
			o = make_response(reply % (user, server, str(int(time.time())), content))		
			o.content_type = 'application/xml'   #
			return o
		else:
			return 'success'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80) 
