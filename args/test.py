#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''
函数参数：必选参数、默认参数、可变参数、关键字参数

参数组合
参数定义的顺序：必选参数、默认参数、可变参数和关键字参数
'''

def func_1(tag, msg):
	print 'tag:', tag, 'msg:', msg

def func_2(tag, msg='hello'):
	print 'tag:', tag, 'msg:', msg

def func_3(*args):
	'''可变参数：就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个在参数前面加上*就是可变参数。
	在函数内部，参数args接收得到的是一个tuple，调用该函数时，可以传入任意个参数，包括0个参数'''
	print type(args)
	print args

def func_4(**kw):
	'''关键字参数
	允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict
	使用**表示关键字参数'''
	print type(kw)
	print kw

#位置传递
func_1('debug', 'debug message')

#关键字传递
func_1(msg='information', tag='info')

#参数默认值
func_2('info')

#可变参数
func_3(1, 2, 3, 4)
test = (5, 6, 7, 8)
func_3(*test)

#关键字参数
func_4(name='tom', id=100)
test = {'name':'alice', 'id':101}
func_4(**test)