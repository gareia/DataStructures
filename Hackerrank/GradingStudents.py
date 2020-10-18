#INPUT array size [1-60]
#      array[i] [0-100]

#OUTPUT array

#TIME COMPLEXITY O(N)

def nextMultipleOf5(number): #[41-99] T: 7 => O(1)
    unit = number % 10 #T: 1
    tens = int(number / 10) #T: 1
    
    if(unit >= 0 and unit < 5): #[0,4] T: 1
        nextMult = tens*10 + 5 #T: 1
    else: #[5-9] T: 1
        nextMult = (tens+1)*10 #T: 1
    
    return nextMult #T: 1

def gradingStudents(grades): #T: 8N+2 => O(N)
    roundedGrades = [] #T: 1
    for grade in grades: #T: N
        if grade < 38 or grade == 100: #T: N
            pass #T: N
        else: #to round grade T: N
            nextMult = nextMultipleOf5(grade) #const T: N
            if(nextMult - grade < 3): #T: N
                grade = nextMult #T: N
        roundedGrades.append(grade)#T: N
    return roundedGrades #T: 1
	
#MAIN
#	gradingStudents call