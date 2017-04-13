#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
lambda 定义了一个匿名函数,因为函数没有名字，不必担心函数名冲突
lambda 并不会带来程序运行效率的提高，只会使代码更简洁。lambda 是为了减少单行函数的定义而存在的。

关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
也可以把匿名函数作为返回值返回
'''

print map(lambda x: x*x, [1, 2, 3])

func = lambda x: x*x
print map(func, [4, 5, 6])

def funcs():
	return [lambda x: x * i for i in range(4)]

for func in funcs():
	print func(2)