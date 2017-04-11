#!/usr/bin/env python 
#coding:utf-8

#类中最常用的方法是实例方法, 即通过通过实例作为第一个参数的方法。
class A(object):	
	def __init__(self, data):
		self.data = data

	def print_data(self):
		print(self.data)

a1 = A('aaa')
a2 = A('bbb')
a1.print_data()
a2.print_data()

#写一个只在类中运行而不在实例中运行的方法
#在Python2.2以后可以使用@classmethod装饰器来创建类方法.
class B(object):
	no_inst = 0
	def __init__(self):
		B.no_inst += 1

	@classmethod
	def get_no_inst(cls):
		return B.no_inst

b1 = B()
b2 = B()
print b1.get_no_inst()
print B.get_no_inst()

#经常有一些跟类有关系的功能但在运行时又不需要实例和类参与的情况下需要用到静态方法
#@staticmethod
IND = 'ON'
class C(object):
	def __init__(self, data):
		self.data = data

	@staticmethod
	def check_ind():
		return (IND == 'ON')

	def func(self):
		if self.check_ind():
			print self.data
c1 = C(1)
c1.func()
print C.check_ind()

