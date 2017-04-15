#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。
subprocess.call(), subprocess.check_call(), subprocess.check_output()
另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。

上面的三个函数都是基于Popen()的封装(wrapper)。
这些封装的目的在于让我们容易使用子进程。当我们想要更个性化我们的需求的时候，就要转向Popen类，该类生成的对象用来代表子进程。

通过使用subprocess包，我们可以运行外部程序。这极大的拓展了Python的功能。
如果你已经了解了操作系统的某些应用，你可以从Python中直接调用该应用(而不是完全依赖Python)，并将应用的结果输出给Python，并让Python继续处理。
shell的功能(比如利用文本流连接各个应用)，就可以在Python中实现。
'''
import subprocess

r = subprocess.call(['ls', '-l'])
print 'Exit code:', r

child = subprocess.Popen(["ping","-c","5","www.baidu.com"])
child.wait()#必须调用对象的wait()方法，父进程才会等待
print("parent process")
'''
child.poll()           # 检查子进程状态
child.kill()           # 终止子进程
child.send_signal()    # 向子进程发送信号
child.terminate()      # 终止子进程
'''

child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)#subprocess.PIPE实际上为文本流提供一个缓存区
child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)
#child2的输出文本也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本。
#communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成。
out = child2.communicate()
print(out)