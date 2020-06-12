#!/usr/bin/env python3

'''
Set examples
'''

# Just declare a set by using {}

unique_vowels = {'a', 'a', 'e', 'o', 'i', 'i', 'i', 'u', 'o'}

print(sorted(unique_vowels))

set_from_string = set('the quick brown fix jumped over the lazy dogs')

# Disgard the space, leaving only the 26 letters
set_from_string.discard(' ')

# Prints the raw set, unordered in {}s
print(set_from_string)
# Sorts the set, returns it in a list in []s
print(sorted(set_from_string))

# Returns an integer of the length
print(len(sorted(set_from_string)))

print()

small_set = set('instafibious')

print(sorted(small_set.intersection(set('instafamous'))))

