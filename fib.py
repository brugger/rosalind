#!/usr/bin/python 
# 
# 
# 
# 
# Kim Brugger (05 Nov 2015), contact: kbr@brugger.dk

import sys
import os
import pprint
pp = pprint.PrettyPrinter(indent=4)

months = 30
litter = 3

serie = [1, 1]

for m in range(2, months ):

    serie.append( serie[ m - 2 ]* litter +  serie[ m- 1] )



pp.pprint( serie )
print serie[ -1 ] 

