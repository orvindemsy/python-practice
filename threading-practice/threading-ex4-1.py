# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:46:18 2020
Threading 4 - Subclassing
https://www.youtube.com/playlist?list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm
@author: user
"""

# According to the docs, the subclassing is recommended to be applied to either
# __int__ method or
# run method
# Still don't get it, let's get back to this later, done half of the vid 11:12
# But there's still some errors in my code


def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))


#This is actually a snippet from threading module
def run(self):
    """Method representing the thread's activity.
    You may override this method in a subclass.
    The standard run() method
    invokes the callable object passed to
    the object's constructor as the
    target argument, if any, with sequential and keyword arguments taken
    from the args and kwargs arguments, respectively.
    """
    
    try:
        if self._target:
            self._target(*self._args, **self._kwargs)
    finally:
        # Avoid a recycle if the thread is running a function
        # an argument that has a member that points to the 
        del self._target, self._args, self._kwargs
            
## TEST1 override/tweak _init_ method
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Thread {} has started".format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a recycle if the thread is running a function
            # an argument that has a member that points to the 
            del self._target, self._args, self.kwargs 
        print('{} has finished!'.format(self.getName()))

for i in range(4):
    t = MyThread(target = sleeper,
                 name = 'thread{}'.format(i+1),
                 args = (3, 'thread{}'.format(i+1)))
    t.start()


    