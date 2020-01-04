# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:54:25 2020
# Daemon
# Using daemon tools to terminate the thread once program reach EOF
https://www.youtube.com/playlist?list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm
@author: orvindemsy
"""

import threading
import time

total = 4

def creates_items():
    global total
    for i in range (10):
        time.sleep(2)
        print('added item by function1')
        total += 1
    print('creation 1 is done')

def creates_items_2():
    global total
    for i in range(7):
        time.sleep(2)
        print('\nadded item by function2')
        total += 1
    print('creation 2 is done')

def limits_items():
    global total
    while True:
        if total > 5:
            print("overloaded")
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(1)
            print("waiting")

creator1 = threading.Thread(target=creates_items)
creator2 = threading.Thread(target=creates_items_2)
# this can only work when run in command prompt not python console
limitor = threading.Thread(target=limits_items, daemon=True)

print(limitor.isDaemon())

creator1.start()
creator2.start()
limitor.start()

creator1.join()
creator2.join()

print('our ending valur of total is', total)
        