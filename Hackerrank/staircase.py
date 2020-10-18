
#Example
#n= 4

#---* i=1
#--** i=2
#-*** i=3
#**** i=4

#Big O(n^2)

def staircase(n): #5N+3NS+3NH => 5N+3N(H+S) => 5N+3N*N => O(N^2)
    #H+S = N
    for i in range(1, n+1): #N
        stringRow = "" #N
        spaces = n - i #N
        hashes = i #N
        while spaces > 0: #N*S
            stringRow += ' ' #N*S
            spaces -= 1 #N*S
        while hashes > 0: #N*H
            stringRow += '#' #N*H
            hashes -= 1 #N*H
        print (stringRow) #N
		
#Main function
	#Input
	#n: integer 1-100
	
	#staircase(n)

