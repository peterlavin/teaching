'''
Created on 1 Sep 2019

@author: peter
'''

from search_for_chars import search_for_chars
    
if __name__ == '__main__':
    
    # Print the help as per the docstrings in the method, NB no args used
    
    print(help(search_for_chars))
    for vals in search_for_chars('are you the hitch-hiker to the galaxy?', 'abcef'):
        print(vals)
    
    print()
    
    for vals in sorted(search_for_chars('now I know my abc, and my ?ei??u')):
        print(vals)
    
    print()
    
    for vals in search_for_chars(target_set='q',phrase='the quick brown fox'):
        print(vals)
    
        
        
    

    
