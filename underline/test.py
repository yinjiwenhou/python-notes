#!/usr/bin/env python 
#coding:utf-8

'''
_、__和__xx__的区别:
_单下划线开头：弱“内部使用”标识，如：”from M import *”，将不导入所有以下划线开头的对象，包括包、模块、成员
单下划线结尾_：只是为了避免与python关键字的命名冲突
__双下划线开头：模块内的成员，表示私有成员，外部无法直接调用
__双下划线开头双下划线结尾__：指那些包含在用户无法控制的命名空间中的“魔术”对象或属性，
如类成员的__name__ 、__doc__、__init__、__import__、__file__、等。
推荐永远不要将这样的命名方式应用于自己的变量或函数。
'''

class Demo(object):
	
	_msg = 'Hello World'
	__default_msg = 'Default message'

	def __init__(self):
		print 'init function'

	def _print_msg(self, msg):
		if len(msg) == 0:
			msg = _msg
		print msg

	def set_msg(self, msg):
		_msg = msg

	def __get_msg(self):
		return self._msg

demo = Demo()

try:
	print demo.__default_msg
except Exception,e:
	#'Demo' object has no attribute '__default_msg'
	print e.message

try:
	print demo.__get_msg()
except Exception, e:
	#'Demo' object has no attribute '__get_msg'
	print e.message



	
