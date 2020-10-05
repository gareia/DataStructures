
#Example
#n= 4

#---* i=1
#--** i=2
#-*** i=3
#**** i=4

#Big O(n^2)

def staircase(n):
    
    for i in range(1, n+1):
        stringRow = ""
        spaces = n - i
        hashes = i
        while spaces > 0:
            stringRow += ' '
            spaces -= 1
        while hashes > 0:
            stringRow += '#'
            hashes -= 1
        print (stringRow)
		
#Main function
	#Input
	#n: integer 1-100
	
	#staircase(n)

