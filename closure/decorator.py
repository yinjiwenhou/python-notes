#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
'''

def decorator(func):
	def wrapper(name, age):
		return func(name, age)
	return wrapper

@decorator
def function(name, age):
	print 'name:', name, ' age:', age

function('tom', 100)


'''
带参数的装饰器
'''
def name_deco(name='tom'):
	def decorator(func):
		def wrapper(age):
			print 'name:', name
			return  func(age)
		return wrapper
	return decorator

@name_deco('Tom')
def age_func(age):
	print 'age:', age

age_func(100)

'''
装饰器是可以叠加使用的，那么这是就涉及到装饰器调用顺序了。对于Python中的”@”语法糖，装饰器的调用顺序与使用 @ 语法糖声明的顺序相反。
'''