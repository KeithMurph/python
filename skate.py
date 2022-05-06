import random
from time import sleep

trickList = [" 'list' to view tricks 'ol' to ollie 'kf' to kickflip 'hf' to heelflip 'bssh' backside shuv 'fssh' frontside shuv 'tre' to treflip 'exit' to exit"]
odds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
game_active = True
print('welcome to the game enter tricks')
print(trickList)
health = (10)
lineBonus = (0)
while game_active == True:
    sleep(.5)
    print('enter trick:')

    trickSelection = str.lower(input())

    if trickSelection == 'ol':
        if random.choice(odds) >= 30:
            print('OLLIE 🛹 up a curb')
            lineBonus = lineBonus + 1
            print('you have', lineBonus, 'line bonus')
        else:
            print('slipped and hit your head')
            health = health - 1
            print('you have', health, 'health left')
            lineBonus = 0
       


    if trickSelection == 'kf':
        if random.choice(odds) >= 50:
            print('KICKFLIP 🛹 on flat')
            lineBonus = lineBonus + 1
            print('you have', lineBonus, 'line bonus')
   
        else:
            print('landed on truck and rolled ankle')
            health = health - 1
            print('you have', health, 'health left')
            lineBonus = 0

    if trickSelection == 'hf':
        if random.choice(odds) >= 60:
            print('HEELFLIP 🛹 down 6 stair')
            lineBonus = lineBonus + 1
            print('you have', lineBonus, 'line bonus')
   
        else:
            print('Creditcard!!!') 
            health = health - 1
            print('you have', health, 'health left')
            lineBonus = 0

    if trickSelection == 'bssh':
        if random.choice(odds) >= 40:
            print('Shuvit 🛹 over trashcan')
            lineBonus = lineBonus + 1
            print('you have', lineBonus, 'line bonus')
    
        else:
            print('shinner!')
            health = health - 1
            print('you have', health, 'health left')
            lineBonus = 0

    if trickSelection == 'fssh':
        if random.choice(odds) >= 50:
            print('Huge Front Shuvit 🛹')
            lineBonus = lineBonus + 1
            print('you have', lineBonus, 'line bonus')
    
        else:
            print('stuck it!')  
            health = health - 1
            print('you have', health, 'health left')      
            lineBonus = 0

    if trickSelection == 'tre':
        if random.choice(odds) >= 75: 
            print('Steezy tre flip 🛹')
            lineBonus = lineBonus + 1
            print('you have', lineBonus, 'line bonus')
    
        else:
            print('not even close')
            health = health - 1
            print('you have -❣️ ', health, 'health left') 
            lineBonus = 0

    if trickSelection == 'list':
        print(trickList)

    if health == 0:
        print('you died ☠️')
        game_active = False
        print('game over')

    if lineBonus == 3:
        health = health + 1
        print('you got a line bonus + 1 health ❣️ ', health)    
        lineBonus = 0

    if trickSelection == 'exit':
        game_active = False
        print('goodbye')


          