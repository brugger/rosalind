#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (30 Oct 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

numbers = (5,1,4,2,3)
numbers = (5,2,4,1,3)

increasing = {}
decreasing = {}

pos = 1
for number in numbers:

    if ( number not in increasing ):        
#        numbers_dict[ number ] = {}
        increasing[ number ] = {}
        decreasing[ number ] = {}


#    pp.pprint( numbers_dict )

    for key in (increasing ):
        if ( number < key ):
            decreasing[ key ][ number ] = pos

        if ( number > key ):
            increasing[ key ][ number] = pos

    pos += 1


def collapse_branch( tree, node):

#    print node 

    if ( len(tree[node]) == 0 ): #.keys()):
#        print "found a leaf!"
        return [[node]]

    results = []

    for subnode in  tree[ node ].keys():
        sub_results =  collapse_branch( tree, subnode )
        for sub_result in sub_results:
            results.append( [node] + sub_result )


#    pp.pprint( results )

    return results


pp.pprint( increasing )
        
pp.pprint( collapse_branch( decreasing, 5 ) )
pp.pprint( collapse_branch( increasing, 1 ) )







#pp.pprint( decreasing )


