# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:59:32 2020
Threading 5: Queue-2
@author: orvindemsy
"""

import queue
#import threading
import time

# Priority Queue Example
# Integer data
q = queue.PriorityQueue()

q.put((1, 'Priority 1'))
q.put((2, 'Priority 2'))
q.put((4, 'Priority 4'))
q.put((2, 'Priority 2'))

for i in range(q.qsize()):
    print(q.get()[1])

'''
# Priority Queue Example
# Integer data
q = queue.PriorityQueue()

q.put(1)
q.put(3)
q.put(4)
q.put(2)

for i in range(q.qsize()):
    print(q.get(), end=' ')
'''

'''
# LIFO Example
q = queue.Queue()

for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end=' ')

print('\n')

import queue
q = queue.LifoQueue()

for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end=' ')
'''
