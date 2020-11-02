

def hourglassSum(arr): #O(n^2)
    maxSum = None #-9*7
    for r in range(0,4): #range(4)
        for c in range(0,4):
            suma = arr[r][c]+arr[r][c+1]+arr[r][c+2] #sum(arr[r][c:c+3])
            suma += arr[r+1][c+1]
            suma += arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2]
            if(r==0 and c==0) or (suma > maxSum):
                maxSum = suma

    return maxSum

#MAIN
	#INPUT arr: array
	#i, j [0, 5]
	#arr[i][j] [-9,9]
	
	#OUTPUT maxSum: integer