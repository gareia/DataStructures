def all_factors_of(num, a):
    for elem in a:
        if(num%elem!=0):
            return False
    return True

def factor_of_all(num, b):
    for elem in b:
        if(elem%num!=0):
            return False
    return True

#INPUT
#n,m [1-10]
#a[i], b[j] [1-100]

#OUTPUT
#integer
def getTotalX(a, b): #O(?n + ?m)
    min_range = max(a) #O(n)
    max_range = min(b) #O(m)
    counter = 0

    for elem in range(min_range, max_range+1): #O(?)
        if(all_factors_of(elem, a) and factor_of_all(elem, b)): #O(?n+?m)
            counter += 1

    return counter
	
#MAIN
#	getTotalX call