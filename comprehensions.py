'''
Created on 6 Sep 2019

@author: peter
A selection of datastructure creations and manipulations using for loops,
then using comprehensions 
'''
import csv, pprint
from datetime import datetime

def convertAmPm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')
    
with open('flight_data.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)

print()

with open('flight_data.csv') as data:
    for line in csv.DictReader(data):
        print(line)

with open('flight_data.csv') as data:
    ''' Skip the first line of headings '''
    skipped_line = data.readline() 
    flights = {}
    for line in data:
        ''' Split each individual line into a key and value '''
        key, val = line.strip().split(',')
        ''' Use key and value for each dictionary item/entry '''
        flights[key] = val

print('\nflights dict\n')
pprint.pprint(flights)

flights2 = {}
for k,v in flights.items():
    flights2[convertAmPm(k)] = v.title()

print('\nflights2 dict with data convertions\n')
pprint.pprint(flights2)

''' The old way, using a for loop '''
dests = []
for dest in flights.values():
    dests.append(dest.title())

print('\ndests list\n')
pprint.pprint(dests)

''' General form... ['whatever is to be appended' for whatever in datastructure.item/values()] 
N.B no colon is added after the for stm '''    

''' Converting data in these dictionaries to a list using comprehensions 
By changing the bracket type, a set is created '''
dests_listcomp = [dest.title() for dest in flights.values()]
dests_setcomp = {dest.title() for dest in flights.values()}
print()
pprint.pprint(dests_listcomp)
print()
pprint.pprint(dests_setcomp)

''' from for stm above where flights2 is created... '''
# for k,v in flights.items():
#     flights2[convertAmPm(k)] = v.title()
''' k colon v space for k comma v in... '''
flights_distcomp = {k:v for k,v in flights.items()}
print()
pprint.pprint(flights_distcomp)

''' By reversing k & v, the cardinality of the entries changes, 
becoming similar to a set, note the loss of some data '''
flights_distcomp_rev = {v:k for k,v in flights.items()}
print()
pprint.pprint(flights_distcomp_rev)

flights_distcomp_filter = {k:v for k,v in flights.items() if v == 'TREASURE CAY'}
print()
pprint.pprint(flights_distcomp_filter)


dests_set = set(flights2.values())
print(dests_set)

wests = []
for k,v in flights2.items():
    if v == 'West End':
        wests.append(k)

print()
print(wests)

''' OR... '''

wests2 = [k for k,v in flights2.items() if v == 'West End']
print(wests2)

''' For all destinations... (just printing) '''
print()
for dest in set(flights2.values()):
    print(dest, '->\t', [k for k,v in flights2.items() if v == dest])

print()
times = {}
for dest in set(flights2.values()):
    times[dest] = [k for k,v in flights2.items() if v == dest]
    
pprint.pprint(times)
''' The above can be done as a comp also, this is not that readable
but works. Nested comprenhensions are optional!!! 

N.B the colon after the name of the dict key here
'''
times2 = {dest: [k for k,v in flights2.items() if v == dest] for dest in set(flights2.values())}

print('\nOutput from inner and outer comp...')                                                                         
pprint.pprint(times2)

''' Small set example, i.e. setcomp '''

print('\n ----------------------------')

vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget your shovel"

found = set()
for v in vowels:
    if v in message:
        found.add(v)
        
        ''' OR... '''

found_comp = {v for v in vowels if v in message}
print(found)
print(found_comp)                                                              
                                                                             