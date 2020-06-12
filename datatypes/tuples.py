'''
Created on 31 Aug 2019

@author: peter
'''

if __name__ == '__main__':
    
    # Immutable tuples
    # Saves on overhead associated with mutable datatypes
    # where the data will never need to change anyway
    
    tuple_0 = ('Python')
    
    print(type(tuple_0))
    
    tuple_1 = ('Python',)   # << a tuple must have at least one comma,
                            # however, it can contain one object
    
    print(type(tuple_1))
    