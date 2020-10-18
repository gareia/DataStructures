#A: ELEMENTS IN APPLES[]
#O: ELEMENTS IN ORANGES[] 
#4+3A+3O => O(A+O)

def countApplesAndOranges(s, t, a, b, apples, oranges): 
    countApples = 0 #T 1
    countOranges = 0 #T 1
    #calcular donde caeran cada una de las manzanas
    for d_apple in apples: #T A
        #ver si esta dentro de la casa
        if(d_apple > 0) and ((a+d_apple) >= s) and ((a+d_apple) <= t): #T A
            countApples += 1 #T A
    #imprimir resultado manzanas
    #sys.stdout.write(countApples)
    print(countApples) #T 1

    #calcular donde caeran cada una de las naranjas
    for d_orange in oranges: #T O
        #ver si esta dentro de la casa
        if(d_orange < 0) and ((b+d_orange) <= t) and ((b+d_orange) >= s):#T O 
            countOranges += 1 #T O
    #imprimir resultado naranjas
    print(countOranges) #T 1
	
#MAIN

	#Input
	#s,t,a,b,m,n [1,10^5]
	#d [-10^5, 10^5] 
	
	#Example
	#a<s<t<b 1<2<3<4
	#m1 n1 d0