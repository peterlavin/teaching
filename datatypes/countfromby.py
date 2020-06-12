'''
Created on 14 Dec 2019

@author: lavinpe
'''



class CountFromBy(object):
    '''
    classdocs
    '''


    ''' This syntax is used because when I type obj.increase(),
    the interpreter does... CountFromBy.increase(obj), therefore
    the method is passed the object itself (similar to this in Java '''
    def increase(self) -> None:
        ''' The self.val etc. syntax applies this change to the
        instance of the object being called/used/changed 
        
        Also, seeing 'self' indicates that this is a class method
        and not a function is a procedural script. '''
        self.val += self.incr


    ''' When I instantiate an object of CountFromBy, I pass two 
    initial args for initial values, these are passed here '''
    def __init__(self, v: int=50, i: int=5):
        
        self.val = v
        self.incr = i
        