#!/usr/bin/python 
# 
# 
# 
# 
# Kim Brugger (07 Nov 2015), contact: kbr@brugger.dk

import sys
import os
import pprint
pp = pprint.PrettyPrinter(indent=4)
import re


def readin_fasta( fasta_file ):

    res = []
    seq = ""
    name = ""

    fasta_fh = open(fasta_file, 'r')
    for line in fasta_fh:
        line = line.strip("\n")
        line = line.strip("\r")

        if ( re.match(">", line)):
            if ( name ):
                res.append( [name, seq] )
            
            name = re.sub(">", "", line)
            seq  = ""

        else:
            seq += line

                           
    if ( name ):
        res.append( [name, seq] )

    return res



fastas = readin_fasta( sys.argv[1] )

consensus_count = []
index = {
    'A' : 0,
    'C' : 1,
    'G' : 2,
    'T' : 3 }

for k in index:
    consensus_count.append([0]*len( fastas[0][1] ))

for fasta in fastas:
    i = 0
    for base in fasta[1]:
        consensus_count[ index[ base ]][ i ] += 1
        i += 1


#pp.pprint( consensus_count )

for base in sorted ( index.keys()):
    print "%s: %s" % ( base, " ".join( map(str, consensus_count[ index[ base]])))

