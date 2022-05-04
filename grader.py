from time import sleep




sleep(1)
studentName = str.lower(input('Enter your Name '))
students = ['bob', 'mary', 'joe'] 



if studentName in students:
    print('Welcome back ', studentName)
    
elif studentName not in students :
    print('hmm ', studentName, ' you say') ; sleep(.9)
    print('You must be a new student ') ; sleep (.5)
    print('lets add you to the list ')
    print(students)    
    students.append(studentName)



sleep(.5)




print(students)

if studentName in students:
    print ("Please enter your test score:")
grade = int(input())

if int(grade) in range(90, 100):
    print ("Great Work! 'A'")
elif int(grade) in range(80, 89):
     print ("Good Job! 'B'")
elif int(grade) in range(70, 79):
     print ("Almost there. 'C'")
elif int(grade) in range(60, 69):
     print ("Needs a lot of work. 'D'")
else:
     print ("Not even close! 'F'")
