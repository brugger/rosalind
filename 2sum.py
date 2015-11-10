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

    counts = {}
    
    i = 1
    found_pair = 0
    for element in map(int, line.split(" ")):

#        print element

        opp_element = -1*element
#        print opp_element
#        pp.pprint( counts )
        if ( opp_element in counts ):
            print "%d %d" % (counts[ -element], i)
            found_pair = 1
            break

        else:
            counts[ element ] = i

        i += 1

    if ( not found_pair ):
        print "-1"


#    print "----"
