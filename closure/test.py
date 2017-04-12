#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数。
个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。

一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。
这个返回的函数B就叫做闭包。你在调用函数A的时候传递的参数就是自由变量。

使用闭包:
第一种场景，在python中很重要也很常见的一个使用场景就是装饰器
第二个场景，就是基于闭包的一个特性——“惰性求值”。
'''

def func(name):
	def inner_func(age):
		print 'name:', name, ' age:', age
	return inner_func

f = func('tom')
f(25)