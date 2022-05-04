from time import sleep

# Grader asks for student name checks class list thae grades

sleep(1)
studentName = str.lower(input('Enter your Name '))
students = ['bob', 'mary', 'joe']
favoriteStudents = ['harry potter']


if studentName in students:
    print('Welcome back ', studentName)

elif studentName not in students :
    print('hmm ', studentName, ' you say') ; sleep(.9)
    print('You must be a new student ') ; sleep (.5)
    print('lets add you to the list ')
    print(students)
    students.append(studentName)
    print(students)
sleep(.5)

if studentName in students:
    print ("Please enter your test score:")
grade = int(input())
if int(grade) ==100:
    print('PERFECT SCORE!')
    favoriteStudents.append(studentName)
    sleep(1)
    print("TOP STUDENTS:", favoriteStudents )
elif int(grade) >=90:
    print ("Great Work! 'A'")
elif int(grade)>= 80:
     print ("Good Job! 'B'")
elif int(grade) >=70:
     print ("Almost there. 'C'")
elif int(grade) >=60:
     print ("Needs a lot of work. 'D'")
else:
     print ("Not even close! 'F'")
     print("you will be missed")
     sleep(.5)
     print(students)
     sleep(1)
     students.remove(studentName)
     print(students)

     
