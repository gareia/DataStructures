#input
#array 
#n = size(array) 1-10^5
#array[i] 1-10^7

#output 
#integer count(max(array))

#priority queue: logn+n = logn
#list.sort: nlogn+n = nlongn
#max + count(max) n

#3 2 1 3 -> 3 3 2 1
#1 1 1 1 -> 1 1 1 1

def birthdayCakeCandles(candles):#5N+3+NLOGN => O(NLOGN)

    maxCount = 0 #1
    candles.sort(reverse=True) #NlogN
    maxHeight = candles[0] #1
    for i in candles: #N
        if(i == maxHeight): #N
            maxCount += 1 #N
        else: #N
            break #N
    return maxCount #1

#MAIN
#	birthdayCakeCandles call
