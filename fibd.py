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

months = 6
life   = 3

serie = [1, 1 ]

for m in range(2, months ):

    if (m < life):
        serie.append( serie[ m - 1 ] +  serie[ m - 2] )
    else:
        serie.append( serie[ m - life + 1 ] +  serie[ m - life] )



pp.pprint( serie )

print serie[ -1 ] 

