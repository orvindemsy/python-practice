# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:43:45 2020
Source:
# Threading 1: Basic
https://www.youtube.com/playlist?list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm
@author: orvindemsy
"""

import threading
import time

def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))
   
# Initializes a thread
t = threading.Thread(target=sleeper, name='thread1', args=(5, 'thread1'))

t.start()
t.join()

print('hello')
print('hello')