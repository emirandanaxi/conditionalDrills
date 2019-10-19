'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
grade = 80
if grade > 65:
    print("passing grade")
'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
grade = 45
if grade < 65:
    print ("failing grade")
else:
    print ("failing grade")
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
age = 18
if age > 17:
    print("able to vote")
else:
    print("able to vote")
'''
#4)Create a variable called weight. Make an if statement that checks the unit of the weight. If the weight is in kilograms, convert it to pounds 
'''
weight = 100
if type(weight) == int:
    print (weight*0.45395)
'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
weight = 4.5
if type(weight) == float:
    print (weight/0.45395)
'''
#6)create a list (seat1 = 1, seat2 = 1, seat3 = 0, seat4 = 1), Now make an if elseif, else statement that checks if a seat is open. if the seat = 1 its closed and print that it's closed. If the seat = 0, it's open and print that it's open. If no seats are open print "There are no available seats"
'''
seat1 = 1
seat2 = 1
seat3 = 0
seat4 = 1
listSeats = [seat1, seat2, seat3, seat4]
if seat1 == 0:
    print ("seat is open")
elif seat1 == 1:
    print ("seat is closed")
if seat2 == 1:
    print ("seat is closed")
elif seat2 == 0:
    print ("seat is open")
if seat3 == 1:
    print ("seat is closed")
elif seat3 == 0:
    print ("seat is open")
if seat4 == 1:
    print ("seat is closed")
elif seat4 == 0:
    print ("seat is open")
 