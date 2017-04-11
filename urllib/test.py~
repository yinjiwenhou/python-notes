#!/usr/bin/env python 
#coding:utf-8
'''
urllib 和 urllib2 (Python2中)的使用及区别:
1.在python中，urllib和urllib2不可相互替代的。 
2.整体来说，urllib2是urllib的增强，但是urllib中有urllib2中所没有的函数。
3.urllib2可以用urllib2.openurl中设置Request参数，来修改Header头。如果你访问一个网站，想更改User Agent（可以伪装你的浏览器），你就要用urllib2.
4.urllib支持设置编码的函数，urllib.urlencode,在模拟登陆的时候，经常要post编码之后的参数，所以要想不使用第三方库完成模拟登录，你就需要使用urllib。
5.urllib一般和urllib2一起搭配使用。
'''

import urllib
import urllib2

u = urllib.urlopen('https://www.baidu.com')
#返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息；
print u.info()

#返回Http状态码。如果是http请求，200表示请求成功完成;404表示网址未找到；
print u.getcode()

#返回请求的url
print u.geturl()

#read()
#readline()
#readlines()
#fileno()
#close()

for line in u:
	print line
u.close()

#urllib.quote(string[, safe])：  对字符串进行编码。参数safe指定了不需要编码的字符;
#urllib.unquote(string) ：       对字符串进行解码；
#urllib.quote_plus(string [ , safe ] ) ：  与urllib.quote类似，但这个方法用'+'来替换' '，而quote用'%20'来代替' '
#urllib.unquote_plus(string ) ：     　　对字符串进行解码；
#urllib.urlencode(query[, doseq])：　　将dict或者包含两个元素的元组列表转换成url参数。{'name': 'dark-bull', 'age': 200}->"name=dark-bull&age=200"
#urllib.pathname2url(path)：        　　 将本地路径转换成url路径；
#urllib.url2pathname(path)：         　　将url路径转换成本地路径

import urllib2
#urllib2.urlopen(url[, data][, timeout])与urllib的函数一样
#urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])，
#url:是网址、文件路径、ftp路径
#　　　　　　data：通过urllib.urlencode形成的字符串。
#　　　　　　header:请求头
#　　　后两个参数：用于第三方的cookie，

