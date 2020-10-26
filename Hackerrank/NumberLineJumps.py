

def kangaroo(x1, v1, x2, v2): #TC: O(1)
    #0, nulls, empty
    answer=""
    if(x2<x1): 
        answer = "FUCK YOU LIAR CONSTRAINT"
    elif(x2>x1 and v2>=v1):
        answer = "NO"
    else:
        residuo = (x2-x1)%(v1-v2)
        answer="YES" if residuo == 0 else "NO"
    return answer
	
def MAIN:

	#X [0 - 10 000]
	#X2 > X1 1 > 0
	#V1, V2 [1 - 10 000]
	
	#kangaroo() is called