#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	File name: myWirelessRouter.py
	Author: xu42 <https://github.com/xu42>
	Date created: 04/04/2016
	Python Version: 3.5

	监测某台无线设备是否接入路由器, 同时猜解当前任务
	适用于 Mercury MW310R 型号的无线路由器
'''


import http.client
import base64
import re
import time

# 配置参数
# url: 路由器后台登陆地址
# port: 路由器后台登陆地址端口
# timeout: 超时
# password: 路由器后台登陆密码
# mac_address: 需要监测的设备的MAC地址
# payload: ajax请求时发送的数据, 请忽视
config = {
	'url': '123.123.123.123',
	'port': '80',
	'timeout': 20,
	'password': '123456',
	'mac_address': '11:11:11:11:11:11',
	'payload': '[LAN_WLAN_ASSOC_DEV#0,0,0,0,0,0#0,0,0,0,0,0]0,4\r\nAssociatedDeviceMACAddress\r\nX_TP_TotalPacketsSent\r\nX_TP_TotalPacketsReceived\r\nX_TP_HostName\r\n'
	}

# 构造请求头部
def __setHeaders():
	headers = {
	'cookie': 'Authorization=Basic ' + base64.b64encode(config['password'].encode('utf-8')).decode('utf-8'),
	'referer': config['url']
	}
	return headers

# 发起请求
def __initRequest():
	conn = http.client.HTTPConnection(config['url'], config['port'], config['timeout'])
	conn.request('POST', "/cgi?5", config['payload'], __setHeaders())
	res = conn.getresponse()
	if res.status != 200:
		print(res.status, res.reason)
		exit()
	data = res.read()
	conn.close()
	return data.decode('utf-8')

# 解析当前接入设备和接收发送数据包量
def __getAssociatedDevice():
	a = re.findall(r"=(.+?)\s", __initRequest())
	# device_list = zip(a[::3], a[1::3], a[2::3])
	return a

# 判断某一设备是否在线
def __isOnline(MACAddress):
	device_list = __getAssociatedDevice()
	try:
		device_list.index(MACAddress)
		return True
	except ValueError:
		return False

# 猜解当前在做什么
def __doWhat(MACAddress = config['mac_address']):
	if __isOnline(MACAddress):
		print("已连入WIFI...")
		print("正在猜解当前在做...")
		device_list_1 = __getAssociatedDevice()
		time.sleep(10)
		device_list_2 = __getAssociatedDevice()
		index_1 = device_list_1.index(MACAddress)
		index_2 = device_list_2.index(MACAddress)
		less = int(device_list_2[index_2 + 2]) - int(device_list_1[index_1 + 2])

		if less < 5:
			print("10s内接收数据包:", less, ",可能连着WIFI什么也没做...")
		elif less < 30:
			print("10s内接收数据包:", less, ",可能聊着QQ...")
		else:
			print("10s内接收数据包:", less, ",可能刷微博|看视频...")

	else:
		print("没有连入WIFI...")


def main():
	__doWhat()
	

if __name__ == '__main__':
	main()
