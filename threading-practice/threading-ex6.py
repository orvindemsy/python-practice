# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:59:32 2020
Threading 5: Queue
@author: orvindemsy
"""

import queue
import threading
import time

def putthing_thread(q):
    while True:
        print('starting thread')
        time.sleep(10)
        q.put(5)
        print('put something')

q = queue.Queue()
t = threading.Thread(target=putting_thread, args(q), daemon = True)
t.start()
q.put(5)

print(q.get())
print("First element fetched")

print(q.get())
print("finished") 

#print(q.empty())
#
#
#for i in range(5):
#    q.put(i)
#    
#while not q.empty():
#    print(q.get(), end=' ')
#
#

