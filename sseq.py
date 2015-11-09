#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (09 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

import re
import rosalind

fastas = rosalind.readin_fasta( sys.argv[ 1 ])

seq   = fastas[ 0 ][ 1 ]
motif = fastas[ 1 ][ 1 ]
#print seq
#print motif

res = []

j = 0
for i in range(0, len( seq )):

    if (seq[ i ] == motif[ j ]):
        res.append( i + 1 )
        j += 1
        if ( j > len(motif) - 1):
            break



print " ".join(map( str, res ))
