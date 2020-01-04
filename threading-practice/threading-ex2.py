# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:58:48 2020
Threading 2: multiple threads
Source:
https://www.youtube.com/playlist?list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm
@author: orvindemsy
"""

import threading
import time

def sleeper(n, name):
    print('{} is starting. Going to sleep for 5 seconds\n'.format(name))
    time.sleep(n)
    print('{} has woken up\n'.format(name))

t = threading.Thread(target=sleeper, args=('babi', 5))

   
# Initializes a thread
# t = threading.Thread(target=sleeper, name='thread1', args=(5, 'thread1'))

# t.start()

threads_list = []


start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper, name='thread {}'.format(i),
                         args=(5, 'thread {}'.format(i)))
    threads_list.append(t)
    t.start()
    print('{} has started \n'.format(t.name))
    
for t in threads_list:
    t.join()
    
end = time.time()

print('time take: {}\n'.format(end-start))

print('All five tasks have finished')