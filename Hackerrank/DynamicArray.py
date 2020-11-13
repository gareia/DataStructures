#INPUT
#n, q [1-10^5]
#1|2 x y [0-10^9] index [0-n-1]
def dynamicArray(n, queries):
    
    seqs = [ [] for _ in range(n) ]
    lastAnswer = 0
    answers = []
    
    for q in queries:
        
        index = ((q[1]^lastAnswer)%n)
        #print("lastAnswer: "+str(lastAnswer))
        #print("index: "+str(index)+" - 1|2: "+str(q[0]))
        
        if(index < n):
            
            if(q[0] == 1):
                seqs[index].append(q[2])
                #print(q[2])
            else: #2
                index_q = (q[2]%(len(seqs[index])))
                lastAnswer = seqs[index][index_q]
                #print("len: "+str(len(seqs[index])))
                #print("lastAnswer: "+str(lastAnswer))
                answers.append(lastAnswer)
        
    return answers
	
#MAIN
#CALL dynamicArray