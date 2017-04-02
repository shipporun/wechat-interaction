# -*- coding: utf-8 -*-

import requests
import json

def fetchWeather(location, number):
	result = requests.get('https://api.thinkpage.cn/v3/weather/daily.json',
		params={
		'key': '9wijlz8aboje7iff',
		'location': location,
		'start': 0,
		'days': number
		})
	data = result.json()
	return data		

def sortData(data, location, number):
	days = []
	weather = []

	for i in range(0, number):
		days.append(data['results'][0]['daily'][i])

	for i in range(0, number):
 		weather.append('%s %s %s %s~%s°C %s风' % (
   	 	days[i]['date'], location,
    	days[i]['text_day'], days[i]['low'],
    	days[i]['high'], days[i]['wind_direction']))
	return weather

def main():
	historyList = []

	while True:
		key = input('请输入指令或想查询的城市：\n')

		if key == 'help':
			print('输入城市名，获取当前天气\n'
				  '输入help，查看帮助\n'
				  '输入history，查看查询历史\n'
				  '输入quit，退出应用')
		elif key == 'quit':
			print('您查询过：')
			for i in set(historyList):
				print(i)
			print('感谢使用。')
			exit()
		elif key == 'history':
			print('查询记录：')
			for i in set(historyList):
				print(i)
		else:
			data = fetchWeather(key, 3)

			if 'status' in data:
				print('No result. Need help?')
			else:
				weather = sortData(data, key, 3)
				i = input('请输入想查询的日期：\n 1 = 今天 2 = 明天 3 = 后天 4 = 三天\n')
				while True:
					try:
						i = int(i) - 1
						if i in [0 ,1 ,2]:
							print(weather[i])
							historyList.append(weather[i])
							break
						elif i == 3:
							a = '\n'.join(weather)
							print(a)
							historyList.append(a)
							break
						else:
							i = input('无结果，请直接输入数字\n范围：1~4\n')
					except ValueError:
						i = input('无结果，请直接输入数字\n范围：1~4\n')

if __name__ == '__main__':
	main()
