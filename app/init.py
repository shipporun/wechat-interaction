# -*- coding:utf8 -*-
from flask import Flask
from flask import request
import hashlib

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def wechat_auth():
	if request.method == 'GET':
		if len(request.args) > 3:
			return make_response(echostr) # what for?
		else:
			return 'Wanna get something?'
	else:
		return 'say hi to captain Butler'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
