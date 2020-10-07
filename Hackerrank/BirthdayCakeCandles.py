#input
#array 
#n = size(array) 1-10^5
#array[i] 1-10^7

#output 
#integer count(max(array))

#if(size == 1):
#    return array[0]

#priority queue: logn+n = logn
#list.sort: nlogn+n = nlongn
#max + count(max) n

#3 2 1 3 -> 3 3 2 1
#1 1 1 1 -> 

def birthdayCakeCandles(candles):
    # Write your code here

    maxCount = 0
    candles.sort(reverse=True) #nlogn
    maxHeight = candles[0]
    for i in candles: #wc: n
        if(i == maxHeight):
            maxCount += 1
        else:
            break
    return maxCount

#Main
