# Python scripts

----------------------------------------

## CET
### 实现功能
获取大学英语四六级成绩。数据来源 [学信网][1]
Windows CMD下因编码问题造成程序出错退出运行，Windows下可在cygwim下运行
###如何使用
```  shell
$ python cet.py
Please input your Name:张三
Please input your Admission Ticket:123456789101112
# 信息将会在这里显示
```

## a_user_agent
### 实现功能
随机返回一个HTTP Request Headers中的`User-Agent`字段(string)
### 如何使用
``` python
1. 在你的项目中 import a_user_agent
2. 在需要使用 User-Agent 的地方调用 a_user_agent.get() 
```
例如：构造一个请求头 headers = {'User-Agent': a_user_agent.get()} 

## proxy_list
### 实现功能
获取网络上的HTTP代理信息。数据来源 [快代理][2]
### 如何使用
``` python
1. 在你的项目中 import proxy_list , 
2. 在需要使用代理的地方调用 proxy_list.get([type]) 返回list格式数据,
3. type 为可选项, inha 国内高匿代理, intr 国内普通(透明)代理, outha 国外高匿代理, outtr 国外普通(透明)代理, 为其他值时获取以上全部，默认值为 intr
```
注：
  1. 依赖于`a_user_agent`
  2. 返回的数据格式为 list ` ['140.75.154.97:8090', '223.150.227.76:9000']`
  3. `__kuaidaili_pages`值为获取的页数，每页大约15条记录
  4. 若`__kuaidaili_pages = 2`且`proxy_list.get('all')`，则返回`2 x 4 x 15 = 120`条记录
  5. 源站可能间歇性无法访问或程序本身存在BUG，返回的记录数量也可能跟理论值有偏差，甚至返回空



[1]:  http://www.chsi.com.cn/cet/
[2]: http://www.kuaidaili.com/free/
