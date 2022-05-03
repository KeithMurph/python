print('Hello World!')

# name + age

name = input('What is your name? ')
print('Hello, ' + name + '!')

age = int(input('How old are you? '))

if age > 18:
    print('You are old enough!')

else:
    print('Get outta her kid!')
    exit()

# number guess
5
print('Please guess a number between 1 and 10: ')
guess = int(input())

if guess == 5:
    print('You guessed it!')
elif guess < 5:
    print('Too low!')
else:
    print('Too high!')

# fruits
fruits = ['apple', 'banana', 'cherry']    

answer = input('What is your favorite fruit?')

if answer == 'apple':
    print('lame')
elif answer == 'banana':
    print('nice')
else:
    print('never heard of it')
