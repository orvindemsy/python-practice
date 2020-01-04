# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:55:06 2020
Threading 4 - Subclassing
https://www.youtube.com/playlist?list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm
@author: orvindemsy
"""

# Still don't get it, will visit this section later 7.50

import threading

class MyThread(threading.Thread):
    def _init_(self, number, style, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style
    
    def run(self, *args, **kwargs):
        print('thread starting')
        
        