'''
Created on 3 Sep 2019

@author: peter
'''
import time


def create_file(name: str, attr: str='r'):
    file_handle = open(name+'.txt', attr)
    return file_handle


if __name__ == '__main__':
    
    ''' Opening file with various options '''
    # First create a file and put something in it.
    # w attribute used to overwrite existing data in file
    
    with open('filename.txt', 'w') as handle:
    
        for num in range(1,6):
            print(f'Line {num} in file', file=handle, end=' | ')
        
        print(end='\n',file=handle)
                
        print('abc', 'xyz', 123, sep='#', file=handle)
        print('def', 'uvw', 456, sep='#', file=handle)

    
    # Read file only
    # existing = create_file('filename', 'r')
    with open('filename.txt', 'r') as ext:
        
        for ln in ext:
            print(ln, end='')
    
    
    