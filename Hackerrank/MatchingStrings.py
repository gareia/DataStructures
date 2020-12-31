
import math
import os
import random
import re
import sys

#len(strings) = n = [1-1000]
#len(queries) = q = [1-1000]
#len(strings[i]) = len(queries[i]) = [1-20] 
def matchingStrings(strings, queries):
    
    d = {}
    for q in queries: #o(queries)
        d[q] = 0
        
    for s in strings: #o(strings)
        val = d.get(s) #o(?)
        if val is not None:
            d[s] += 1
    
    return [d[q] for q in queries] #o(queries)

#MAIN
#input
#n[1-1000] size of strings[]
#q[1-1000] size of queries[]
#len(strings[i]), len(queries[i]) [1-20]

#output
#array of results for each query