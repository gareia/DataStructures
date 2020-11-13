from collections import deque

#INPUT
#arr: array
#n [1-10^5] | n = size(arr)
#d [1-n] 
#arr[i] [1-10^6]
def rotateLeft(d, arr):
    
    n = len(arr)
    
    if d >= n:
        d = d%n #0 return q
        
    if d > n/2:
        d = (n-d)*-1
        
    q = deque(arr)
    
    while(d != 0):
        if(d > 0):
            elem = q.popleft()
            q.append(elem)
            d -= 1
        else:
            elem = q.pop()
            q.appendleft(elem)
            d += 1
    
    return q
   
#MAIN
#CALL rotateLeft