#!/usr/bin/env python3
'''
Created on 13 Dec 2019

@author: lavinpe

Example of using a dictionary to count occurrences of 
letters in a user input string
'''

phrase = input('Type something...\n')
plist = list(phrase)
vowels = ['o','u','i','a','e']
# Define found as a dictionary, this is all that is needed
# NB, insertion order in a dictionary is not maintained
found  = {}

for letr in plist:
    if letr in vowels:
        # If a letter is found, it must be initialised as 0 in 
        # the dictionary.
        # If it is found, .setdefault returns the existing value, this
        # is then incremented 
        found.setdefault(letr, 0)
        # Set the value of the letter 'key' to be the incremented freq
        found[letr] += 1
        
        '''
        # Alternative, more explicit code, setdefault returns 
        # the existing value, this can then be incremened and set        
        extval = found.setdefault(letr, 0)
        # Set the value of the letter 'key' to be the incremented freq
        found[letr] = extval + 1
        '''

for kv in sorted(found):
    print(kv,'\t', found[kv])

print() 

for k,v in sorted(found.items()):
    # print(k,'\twas found',v,'time(s)')
    print(f"{k}\t was found {v} time(s)")

    
