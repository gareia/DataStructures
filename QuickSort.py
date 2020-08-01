
def qs(array, i, f):
    
    comp = i
    pivot = f
    
    while comp < pivot:
        
        if array[comp]>array[pivot]:
            aux = array[comp]
            if pivot-comp != 1:
                array[comp] = array[pivot-1]
            array[pivot-1] = array[pivot]
            array[pivot] = aux
            pivot -= 1
            
        else:
            comp += 1
    
    if pivot != i:
        qs(array, i, pivot-1)
    if pivot != f:
        qs(array, pivot+1, f)
    
    

def quicksort(array):
    
    #array, inicio, final
    qs(array, 0, len(array) -1)
    
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)