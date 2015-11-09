#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (09 Nov 2015), contact: kim@brugger.dk

import sys
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)



#
# reverse compliments a DNA string
#
#
# Kim Brugger (09 Nov 2015), contact: kbr@brugger.dk
def rev_comp( dna ) :

    revbase = { 'A' : 'T', 
                'C' : 'G', 
                'G' : 'C',
                'T' : 'A'}

    revdna = [""]*len(dna)

    dna_len = len( dna )

    for i in range(0, len(dna)):                

        revdna[ dna_len - i - 1] = revbase[ dna[ i ] ]

    return "".join(revdna)




#
# reads in a fasta file and returns it as an array of arrays
#
#
# Kim Brugger (09 Nov 2015), contact: kbr@brugger.dk
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




#
# reads in a fasta file and returns it as an array of arrays
#
#
# Kim Brugger (09 Nov 2015), contact: kbr@brugger.dk
def DNA2AA( DNA ):

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
    


    
    DNA = DNA.replace("T", "U")

    AAs  = ""
    for i in range(0, len(DNA), 3):
        codon = DNA[i: i+3]
        if ( codon in codon2AA ):
            AAs += codon2AA[ codon ]
        else:

            AAs += "X"

    return AAs
