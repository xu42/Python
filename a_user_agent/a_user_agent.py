# -*- coding: utf-8 -*-
'''
  WHAT:
    get a random User-Agent
    return a string 

  HOW TO USE:
    import a_user_agent
    a_user_agent.get()

'''

from random import sample

__user_agent = []

def __set_user_agent_list():
    __user_agent.append('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    __user_agent.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36')
    __user_agent.append('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')
    __user_agent.append('Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))')
    __user_agent.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)')
    __user_agent.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    __user_agent.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    __user_agent.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    __user_agent.append('Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0')
    __user_agent.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0')
    __user_agent.append('Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0')
    __user_agent.append('Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13')
    return

def get():
    __set_user_agent_list()
    return sample(__user_agent, 1)[0]

if __name__ == '__main__':
    print get()
