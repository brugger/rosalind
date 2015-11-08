#!/usr/bin/python 
# 
# 
# 
# 
# Kim Brugger (06 Nov 2015), contact: kbr@brugger.dk

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
#for fasta in  ( fastas ):

pp.pprint( fastas )
