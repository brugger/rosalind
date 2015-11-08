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

dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

codon2AA = { 
    "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
    "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
    "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
    "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
    "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
    "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
    "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
    "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
    "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
    "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
    "UAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
    "UAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
    "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
    "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
    "UGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
    "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" }


def rev_comp( dna ) :

    revbase = { 'A' : 'U', 
                'C' : 'G', 
                'G' : 'C',
                'T' : 'A' }

    revdna = [""]*len(dna)

    dna_len = len( dna )

    for i in range(0, len(dna)):                

        revdna[ dna_len - i - 1] = revbase[ dna[ i ] ]

    return "".join(revdna)


print dna
#dna = rev_comp( dna )
#print dna
dna = dna.replace("T", "U")
AAs  = ""
orf = 0
for i in range(0, len(dna), 3):

    codon = dna[i: i+3]
    if codon not in codon2AA:
        next
    else:
        AA = codon2AA[ codon ]

    print "%s - %s" % (codon, AA )

    if (AA == "M"):
        orf = 1
        AAs += AA

    if ( AA == "*"):
        if (len ( AAs ) > 0):
            print AAs

        AAs = ""
        orf = 0

    if ( AAs != "" ):
        AAs += AA


