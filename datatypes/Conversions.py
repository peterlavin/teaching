'''
Created on 31 Aug 2019

@author: peter
'''

myval = f"125"
mychar = "A"
myhex = 1024
myoct = 512

print(int(myval))
print(float(myval))
print(ord(mychar))
print(hex(myhex))
print(oct(myoct))


this_tuple = "longevity"
print(tuple(this_tuple),'\n')

this_set = "aabbbcddeeeeefh"
print(set(this_set),'\n')  # unique list of values from the above string

mylist = "Peter Lavin"
print(list(mylist),'\n')

print(str(12345),'\n')

print(complex(2,4))


this_list = ['abc', 34, 'xyz',set(this_set)]

print(this_list[2])
this_list.pop(2)
print(this_list)
# this_list.extend(list(mylist))
print(this_list)

import array

this_array = array.array('i', [1,2,3,4])
print(this_array[3])
new_arr = array.array('c')
new_arr.append('w')

