
def binary_search(input_array, value):
    indexInicio = 0
    longitud = len(input_array)
    indexFinal = longitud - 1
    
    while longitud > 1:
        
        if longitud % 2 == 0: #par
            indexMitad = indexInicio + int(longitud/2)-1
        else: #impar
            indexMitad = indexInicio + int(longitud/2)
        
        #print "IndexMitad "+str(indexMitad)
        
        if value == input_array[indexMitad]:
            #print "Se encontro el valor en " +str(indexMitad)
            return indexMitad
        elif value < input_array[indexMitad]:
            indexFinal = indexMitad - 1
            #print "nuevo indexFinal " +str(indexFinal)
        else: #value > inp....[]
            indexInicio = indexMitad + 1
            #print "nuevo indexInicio " +str(indexInicio)
            
        longitud = (indexFinal+1) - indexInicio
    
    if (longitud == 1) and (input_array[indexFinal] == value):
        return indexFinal
    else: #value != inpt[] || longitud  =0
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
