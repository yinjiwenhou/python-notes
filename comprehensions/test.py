#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
列表生成式
运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
'''

print [x*x for x in range(1, 11)]

print [x*x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ']

print [x*y for x in ['a', 'b', 'c'] for y in [1, 2]]