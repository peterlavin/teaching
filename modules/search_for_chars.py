'''
Created on 1 Sep 2019

@author: peter
'''

def search_for_chars(phrase: str, target_set: str='aeiou') -> set:
    """ Return the intersections set of chars found in a two supplied phrases"""
    return set(target_set).intersection(set(phrase))
