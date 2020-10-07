#1 1 1 1 1
#4 | 4

#1 3 4 8 20
#1+3+4+8 | 3+4+8+20

#BigO(sort)

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    answer = ""
    arr.sort()
    minSum = arr[0]+arr[1]+arr[2]+arr[3]
    maxSum = arr[4]+arr[3]+arr[2]+arr[1]
    answer += (str(minSum)+' '+str(maxSum))
    print (answer)

#Main

#input: array & len(array) = 5
#array[i] = 1-10^9