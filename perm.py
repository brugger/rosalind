#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (05 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

size = 7

numbers = range( 1, size + 1)




permuts = []

def return_numbers( sub_perm ):


    res = []
    
    
    if ( len(sub_perm ) == 0):

        for number in numbers:
             res.append( [ number] )
    
        return res

    else:

        for sub in sub_perm:
            for number in numbers:
                if number in sub:
                    continue
                res.append(  [number] + sub )

        return res

        


for i in numbers:
    permuts = return_numbers( permuts )

print len( permuts )

#pp.pprint(  permuts )
for permut in sorted( permuts ):
    print " ".join(map( str, permut))
