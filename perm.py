#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (05 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

size = 3

numbers = range( 1, size + 1)


permuts = []



def add_numbers( numbers ):
    

    number = numbers.pop(0)

    print number


    if len( numbers ) == 0:
        return [[number]]

    res = []


    for sub_permut in add_numbers( numbers ):
        res.append( [number] + sub_permut )
    



    pp.pprint( res )
    return res



pp.pprint( add_numbers( numbers ))
