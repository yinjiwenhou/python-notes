#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print 'Run task %s (%s).' % (name, os.getpid())
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
	print 'Panent process %s.' % os.getpid()
	p = Pool(4)
	for i in xrange(5):
		p.apply_async(long_time_task,args=(i,))
	print 'Waiting for all subprocessing done...'
	p.close()
	p.join()
	print 'All process done.'