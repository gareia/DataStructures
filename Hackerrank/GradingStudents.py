#INPUT array size [1-60]
#      array[i] [0-100]

#OUTPUT array

def nextMultipleOf5(number): #[41-99]
    unit = number % 10
    tens = int(number / 10)
    
    if(unit >= 0 and unit < 5): [0,4]
        nextMult = tens*10 + 5
    else: #[5-9]
        nextMult = (tens+1)*10
    
    return nextMult

def gradingStudents(grades): #O(n)
    roundedGrades = []
    for grade in grades: #O(n)
        if grade < 38 or grade == 100:
            pass
        else: #to round grade
            nextMult = nextMultipleOf5(grade) #const 'cause no loop
            if(nextMult - grade < 3):
                grade = nextMult
        roundedGrades.append(grade)
    return roundedGrades
	
#MAIN
#gradingStudents call