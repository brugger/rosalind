#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (30 Oct 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

numbers = (5,1,4,2,3)
#numbers = (5,2,4,1,3)
numbers = (8, 2, 1, 6, 5, 7, 4, 3, 9)
increasing = {}
decreasing = {}

min = -1
max = -1

for number in numbers:

    if (max == -1 or number > max):
        max = number

    if (min == -1 or number < min):
        min = number

    if ( number not in increasing ):        
        increasing[ number ] = {}
        decreasing[ number ] = {}

    for key in (increasing ):
        if ( number < key ):
            decreasing[ key ][ number ] = 1

        if ( number > key ):
            increasing[ key ][ number] = 1


def collapse_graph( graph, start, end ):

    col_graph = {}
    
    step = 1
    if ( start > end):
        step = -1

    for node in range( start, end, step):

        if ( node not in col_graph):
            col_graph[ node ] = []

        for subnode in graph[ node ].keys():

            if subnode in ( col_graph) and ( len(col_graph[ subnode] ) >= 1 ):
                for subgraph in col_graph[ subnode ]:
                    col_graph[ node ].append( [node] + subgraph )
            else:
                col_graph[ node ].append( [node, subnode] )

    longest_subgraph = []
    longest_subgraphs = []
    
    for start in col_graph:
        for subgraph in col_graph[ start ]:
            if ( len( longest_subgraph ) < len( subgraph )):
                longest_subgraph = subgraph


                # The following is for reporting multiple subgraphs of the same length:
                longest_subgraphs = []
                longest_subgraphs.append( subgraph )
            elif ( len( longest_subgraph ) == len( subgraph )):
                longest_subgraphs.append( subgraph )
                

            

    pp.pprint( longest_subgraphs )

    for i in range(0, len( longest_subgraph)):
        longest_subgraph[ i ]  = str( longest_subgraph[ i ] )



    return longest_subgraph


print "lgis increasing: :  " + ",".join( collapse_graph( increasing, max, min - 1))
print "lgis decreasing: :  " + ",".join( collapse_graph( decreasing, min, max + 1 ))
