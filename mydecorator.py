'''
Created on 5 Sep 2019

@author: peter
'''

from functools import wraps
import random

def get_random_bool():
    return random.choice([True, False])

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ''' The passed in function does not get called if the
        logic does not allow (could be access control, etc. '''
        if get_random_bool():
            return func(*args, **kwargs)
        else:
            print(" *** Test FAILED ***")
    return wrapper

''' This function will only be executed if it is allowed to do so
by my_decorator '''
@my_decorator
def decorated(num: int) -> None:
    print(f'{num} Decorated func was called')

''' Call the decorated(*args) function a number of times '''
for i in range(0,10):
    decorated(i)