#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (09 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

array1 = "2 4 10 18"
array2 = "-5 11 12"


array1 = map(int, array1.split(" "))
array2 = map(int, array2.split(" "))


sorted_array = []

while( array1 or array2 ):
    if ( not array2 ):
        sorted_array.append( array1.pop(0))

    elif ( not array1 ):
        sorted_array.append( array2.pop(0))

    elif ( array1[0] < array2[0]):
        sorted_array.append( array1.pop(0))
    else:
        sorted_array.append( array2.pop(0))



print " ".join( map(str, sorted_array))
