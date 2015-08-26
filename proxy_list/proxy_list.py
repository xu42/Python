#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re
import a_user_agent
# from time import sleep

__kuaidaili_pages = 2 # How many pages need to crawl, There are 15 records per page
__kuaidaili_proxy_list = [] # proxy list for one type, it's empty for failed
__all_kuaidaili_proxy_list = [] # proxy list for all type, it's empty for failed


def get(type = 'inha'):
	if type == 'inha':
		return __get_kuaidaili_free_inha()
	elif type == 'intr':
		return __get_kuaidaili_free_intr()
	elif type == 'outha':
		return __get_kuaidaili_free_outha()
	elif type == 'outtr':
		return __get_kuaidaili_free_outtr()
	else:
		return __get_kuaidaili_free_all()


# get free China highly anonymous proxy by kuaidali.com
def __get_kuaidaili_free_inha():
	url = 'http://www.kuaidaili.com/free/inha/'
	return __carwl_kuaidaili(url, __kuaidaili_pages)

# get free China general anonymous proxy by kuaidali.com
def __get_kuaidaili_free_intr():
	url = 'http://www.kuaidaili.com/free/intr/'
	return __carwl_kuaidaili(url, __kuaidaili_pages)

# get free Foreign highly anonymous proxy by kuaidali.com
def __get_kuaidaili_free_outha():
	url = 'http://www.kuaidaili.com/free/outha/'
	return __carwl_kuaidaili(url, __kuaidaili_pages)

# get free Foreign general anonymous proxy by kuaidali.com
def __get_kuaidaili_free_outtr():
	url = 'http://www.kuaidaili.com/free/outtr/'
	return __carwl_kuaidaili(url, __kuaidaili_pages)

# get all free proxy by kuaidali.com
def __get_kuaidaili_free_all():
	global __all_kuaidaili_proxy_list
	__all_kuaidaili_proxy_list += __get_kuaidaili_free_inha()
	__all_kuaidaili_proxy_list += __get_kuaidaili_free_intr()
	__all_kuaidaili_proxy_list += __get_kuaidaili_free_outha()
	__all_kuaidaili_proxy_list += __get_kuaidaili_free_outtr()
	return __all_kuaidaili_proxy_list

# set request headers for kuaidaili.com
def __set_kuaidaili_headers():
	ua = a_user_agent.get()
	headers = {'User-Agent': ua, 'Referer': 'http://www.kuaidaili.com/'}
	return headers
# main method Crawl 
def __carwl_kuaidaili(url, pages = __kuaidaili_pages):
	for x in xrange(1, pages+1):
		web_page = __get_web_page(url + str(x) + '/')
		global __kuaidaili_proxy_list # it must use keyword 'global',maybe is a bug with Python2
		__kuaidaili_proxy_list  += __regular_resolve_kuaidaili(web_page)
		# sleep(0.1)
	return __kuaidaili_proxy_list

# get page source
def __get_web_page(url):
	try:
		headers = __set_kuaidaili_headers()
		req = urllib2.Request(url, None, headers)
		response = urllib2.urlopen(req, timeout = 3)
		web_page = response.read()
	except Exception, e:
		web_page = ''
	finally:
		response.close()
	return web_page

# regular resolve web page, return a proxy list
def __regular_resolve_kuaidaili(web_page):
	try:
		web_page_tbody = re.findall(r"<tbody>(.*?)</tbody>", web_page, re.S)
		a_proxy_list_ip = re.findall(r"<td>(\d+\.\d+\.\d+\.\d+)</td>", web_page_tbody[0], re.S)
		a_proxy_list_port = re.findall(r"<td>(\d{2,5})</td>", web_page_tbody[0], re.S)
	except Exception, e:
		a_proxy_list_ip = []
		a_proxy_list_port = []
	finally:
		a_proxy_list = []
	
	for x in xrange(0, len(a_proxy_list_ip)):
		a_proxy_list.append(a_proxy_list_ip[x] + ":" + a_proxy_list_port[x])
	return a_proxy_list


if __name__ == '__main__':
	for x in get():
		print x
