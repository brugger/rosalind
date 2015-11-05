#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (05 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC";

def readin_fasta( fasta_file ):

    res = []
    seq = ""
    name = ""

    fasta_fh = open(fasta_file, 'r')
    for line in fasta_fh:
        line = line.strip("\n")

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


def calc_gc( dna ):

    ATs = 0
    GCs = 0

    for i in range(0, len(dna)):

        if ( dna[ i ] == 'A' or dna[i] == 'T'):
            ATs += 1
        elif ( dna[ i ] == 'C' or dna[ i ] == 'G'):
            GCs += 1

    return float(GCs*100)/(GCs+ATs)



fastas = readin_fasta( sys.argv[1] )
pp.pprint( fastas )

for fasta in  ( fastas ):
    print fasta[ 0 ]
    print "%.6f" % calc_gc( fasta[ 1 ])
