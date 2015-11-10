#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (10 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

import rosalind


fastas = rosalind.readin_fasta( sys.argv[ 1 ])



dna1 = fastas[0][1]
dna2 = fastas[1][1]

transversions = 0
transitions   = 0

for i in range(0, len( dna1 )):

    

    base1 = dna1[ i]
    base2 = dna2[ i]

    if ( base1 != base2 ):
        if (((base1 == 'A' or base1 == 'G') and (base2 == 'A' or base2 == 'G')) or 
            ((base1 == 'C' or base1 == 'T') and (base2 == 'C' or base2 == 'T'))):
            transitions += 1
        else:

            transversions += 1


print "%.5f" % (float( transitions)/transversions )


