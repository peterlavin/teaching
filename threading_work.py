'''
Created on 6 Sep 2019

@author: peter
'''

from threading import Thread
import time

''' If you were running this as a thread as part of, say, a HTTP request
in Flask, you should decorate it with @copy_current_request_context 
so that the variables (context) will still be available after the HTTP request
thread has ended, otherwise, it will throw exceptions '''
def can_be_slow(ex_time: int) -> None:
    time.sleep(ex_time)
    print(f'Func can_be_slow() is about to exit after {ex_time} sec.')

print('Run before thread is started')

ex_time = 0.5
''' Note that args must be a tuple, even one value needs a comma '''
th = Thread(target=can_be_slow, args=(ex_time,))

print(th.is_alive())
th.start()

print('Run after thread is started but not blocked by it')

time.sleep(ex_time + 0.1)
print(f'th.is_alive() is {th.is_alive()}')
