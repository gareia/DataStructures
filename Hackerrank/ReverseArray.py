

def reverseArray(a):

    pos0 = 0
    posF = len(a)-1

    while(pos0 < posF): #O(n/2) => O(n)
        aux = a[pos0]
        a[pos0] = a[posF]
        a[posF] = aux

        pos0 += 1
        posF -= 1
    
    return a
	
#MAIN
#	INPUT a: array n: len(a)
#	n [1-10^3] 
# 	a[i] [1-10^4]
#	reverseArray(a) call
#	OUTPUT reversed array