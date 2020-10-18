#1 1 1 1 1
#4 | 4

#1 3 4 8 20
#1+3+4+8 | 3+4+8+20

def miniMaxSum(arr): #5+NLOGN => O(NLOGN)
    answer = "" #1
    arr.sort() #NLOGN
    minSum = arr[0]+arr[1]+arr[2]+arr[3] #1
    maxSum = arr[4]+arr[3]+arr[2]+arr[1] #1
    answer += (str(minSum)+' '+str(maxSum)) #1
    print (answer) #1

#MAIN

#input: array & len(array) = 5
#array[i] = 1-10^9