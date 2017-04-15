#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。

第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
"""
g = (x*x for x in range(1, 11))
print type(g)
for n in g:
	print n

'''
最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)