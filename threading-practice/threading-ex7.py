# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:35:39 2020
Threading 5: Event
@author: orvindemsy
"""

'''
#Events
event = Threading.event()

# Setting the flag to true
event.set()

# Setting the flag to false
event.clear()

# Block the thread from moving forward
# until event.set is called, so if True => Move forward, no longer wait
event.wait()
'''

import queue
import threading
import numpy as np
import time

def flag():
    time.sleep(3)
    event.set()
    print('starting countdown')
    time.sleep(7)
    print('event is cleared')
    event.clear()
    
def start_operations():
     event.wait()
     while event.is_set():
         print('starting random integer task')
         x = np.random.randint(1, 30)
         time.sleep(.5)
         if x == 29:
            print('True')
     
     print('Event has been cleard, random operation stops')

event = threading.Event()
t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=start_operations)

t1.start()
t2.start()

