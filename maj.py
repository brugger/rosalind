#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (10 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

fh = open(sys.argv[1], 'r')

majs = []

fh.readline()
for line in fh:
    line = line.rstrip("\n")

#    print line
    counts = {}
    
    elements = 0
    for element in map(int, line.split(" ")):
        
        if (element not in counts ):
            counts [element] = 0
            
        counts [element] += 1
        elements += 1

    max_value = int(elements/ 2)
    majority  = -1
    for i in counts:
        if (counts[ i ] > max_value ):
            max_value = counts[ i ]
            majority = i


    majs.append( majority )


print " ".join(map( str, majs ))
