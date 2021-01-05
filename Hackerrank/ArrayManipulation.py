
import math
import os
import random
import re
import sys
import heapq

#o(n+m)

# n [3 - 10^7] 30 000 000 m [1 - 2*10^5] 200 000
# a, b [1 - n] a <= b
# k [0 - 10^9]
def arrayManipulation(n, queries):
    
    arr = [0]*n #o(n)
    max_sum = 0
   
    for q in queries: #O(m)
        
        a = q[0]-1
        afterB = q[1]
        k = q[2]
        
        arr[a] += k
        if(afterB < n):
            arr[afterB] -= k
        
    current_sum = 0
    
    for elem in arr: #o(n)
	
        if(elem == 0): continue
		
        current_sum += elem
        if(current_sum > max_sum):
            max_sum = current_sum     
    
    return max_sum