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

fastas = rosalind.readin_fasta( sys.argv[1])

#pp.pprint( fastas )

gene = fastas[0][1]
fastas.pop(0)
for intron in fastas:
    gene = gene.replace(intron[1], "")


#print gene

protein = rosalind.DNA2AA( gene )


print protein[0:-1]
