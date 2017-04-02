# -*- coding:utf8 -*-
from flask import Flask
from flask import request
import hashlib

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def wechat_auth():
	if request.method == 'GET':
		token = 'niceday'
		signature = request.args['signature']
		timestamp = request.args['timestamp']
		nonce = request.args['nonce']
		echostr = request.args['echostr']
		s = [timestamp, nounce, token]
		s.sort() # what for?
		s = ''.join(s)
		if hashlib.sha1(s).hexdigest() == signature :
			return make_response(echostr) # what for?
	else:
		return 'say hi to captain Butler'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
