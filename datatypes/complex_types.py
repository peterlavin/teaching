'''
Created on 31 Aug 2019

@author: peter
'''

if __name__ == '__main__':
    
    people = {}
    print(type(people))
    
    people['Jon'] = {'Name':'Jonny', 'Origin':'Orion', 'Job':'starman'}
    
    print(people['Jon']['Job'])
    print()
    print()
    
    people['Art'] = {'Name':'Arty', 'Origin':'Venus', 'Job':'planetman'}
    people['Janet'] = {'Name':'Jan', 'Origin':'Mars', 'Job':'spaceangel'}
    people['Jean'] = {'Name':'Jeannie', 'Origin':'Earth', 'Job':'astronaut'}
    
    import pprint
    
    pprint.pprint(people)