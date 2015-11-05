#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (05 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

alphabet = ('A','C', 'G', 'T')
alphabet = ('T' ,'A','G', 'C')

length   = 2

alphabet = "T Q G J W H R L F P E I"
alphabet = alphabet.split(" ")

length   = 4


permuts = []

def permutate( sub_perm ):


    res = []
    
    
    if ( len(sub_perm ) == 0):

        for letter in alphabet:
             res.append( [ letter] )

    else:
        for sub in sub_perm:
            if sub not in res:
                res.append( sub )
            for letter in alphabet:
                res.append(  [letter] + sub )


        
    return res


def cmp_kmer(kmer1, kmer2 ):

    for i in range(0, max(len(kmer1), len(kmer2))):
        if ( len( kmer1 ) <= i):
            return -1

        if ( len( kmer2 ) <= i):
            return 1

        if ( kmer1 [ i ] != kmer2[ i ]):
            if (a2s[ kmer1[ i ] ] < a2s[ kmer2[ i ]]):
                return -1
            else:
                return 1


    return 0

def alphabet2score( alphabet ):
    a2s = {}
    for i in range(0, len(alphabet)):
        a2s[ alphabet[ i ] ] = i 

    return a2s


a2s = alphabet2score( alphabet )

for i in range(0, length):
    permuts = permutate( permuts )


permuts = sorted( permuts, cmp = cmp_kmer)

for permut in  permuts  :
    print "".join(map( str, permut))
