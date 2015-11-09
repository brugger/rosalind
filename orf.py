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

import rosalind


dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

dna = "GAGTTTTTAAGTACAGGAATACCTTTTGAGTTCTCAGTTAGAGGATCCGTTAGTGATTGGGCTGACCTAATCGGTCGTATCGCCTCATTCAGTCAGACTTGCGAAACGGGGTGTACGTGATCTTGGTCTATATGTGTTAACACATTGCCATTCTTGCAGAGAGAAGGTGAATGGTTGGCGCCGGACAATGATCGGACGAGTGCTGTTGAGGTATAAGGTGCGCGGGTATCCCAAATTGGAAATTGGAAACGAAAATCCCGCCTCTTACACGAAAGATTACATTTTCGTGAGGTTCCCACGTTAGCAGGTTTGGGCCACCGCTTGCCTAAGTATTTAAACCCGGCGATATGCCGCTCACCGCAAGGTGTCTGGCGCTTGTCCTTCAGTTTGGGGTGAGCTTCTATTGGTGGGTCAAGATGATGACGTACGGGAGGTATTCTACAGGATCCGACCCAGGGAAGTCCCCATGGCTCCGATGGCAGCGCCCTAGCTAGGGCGCTGCCATCGGAGCCATTCCACTTGTCCAATGCGTAAGCCGCCAGTGGTACTAGCGTACGCTTCACTATAAATTAGGGGGTATTGAGAGCCGGGGGGTGCCAGGGGATCCATCCAGGTTGGTAGGCCGGTAAAAACAGCCGCCTCCTAGATCGTTACCGCGACGCTCCGCCCTCGCCCGGTCGCTTCCAACACGGTTTCCTCCGCCTGGTATCTAGACGGATTACCCCGAGAGTGTCAAATCGTAGGACAAAACCTAAGGCCCTGGCTGCAGAATGGCGGAGGAGGGCCGAGAGTCGTGGAATACCAGCCCAAAACAGATAAATCACGCGACCATAGTATATCGCACATACTCCGTACCGAATGAACTACCGACAGGTCATATCAAGCTATGTCCCTGGAGCATCCTTCCCAAGGGACAAATACTTGCCTGGTGGAGCTGCATTAGGAGTTTGTAAAAGCAAGTAGCGTCACTTGTAACGGCA"



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




#print dna

def DNA2AA( DNA ):
    
    DNA = DNA.replace("T", "U")

    AAs  = ""
    for i in range(0, len(DNA), 3):
        codon = DNA[i: i+3]
        if ( codon in codon2AA ):
            AAs += codon2AA[ codon ]
        else:

            AAs += "X"

    return AAs




def find_orfs( DNA ):
    AAs  = DNA2AA( DNA )

#    print AAs 

    ORFs = []

    for i in range(0, len(AAs)):
        if ( AAs[ i ] != "M"):
            continue

        for j in range(i + 1, len(AAs)):
            if ( AAs[ j ] == "*"):
#                print "%d %d" %( i, j)
                ORFs.append( "".join(AAs[i:j]))
                break
                              
    return ORFs
    
        

orfs = {}
for i in range( 0, 3):
#    print i
    
    for orf in find_orfs( dna[i:-1]):
        orfs[ orf ] = 1

dna = rosalind.rev_comp( dna)
for i in range( 0, 3):
    for orf in find_orfs( dna[i:-1]):
        orfs[ orf ] = 1

#orfs = set( orfs)

print "\n".join( orfs.keys() )
