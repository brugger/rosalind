#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (09 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)



def fibo( n ):
   if n == 0: 
       return 0
   elif n == 1: 
       return 1
   else: 
       return fibo(n-1)+fibo(n-2)




print fibo( 25 )
