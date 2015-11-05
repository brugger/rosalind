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

numbers = range(-size, 0) +  range( 1, size + 1)

#pp.pprint( numbers )



permuts = []

def return_numbers( sub_perm ):


    res = []
    
    
    if ( len(sub_perm ) == 0):

        for number in numbers:
             res.append( [ number] )
    

    else:

        for sub in sub_perm:
            for number in numbers:
                if (number in sub or (-1 * number) in sub):
                    continue
                res.append(  [number] + sub )


        
#    pp.pprint( res )
    if ( len( res )):
        return res
    else:
        return sub_perm


for i in numbers:
    permuts = return_numbers( permuts )

print len( permuts )

#pp.pprint(  permuts )
for permut in  permuts  :
    print " ".join(map( str, permut))
