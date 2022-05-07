import random
from time import sleep
from colorama import Fore
# 
trickList = ['ol' , 'kf', 'hf', 'bssh', 'fssh', 'tre']
# trickList = [" 'list' to view tricks 'ol' to ollie 'kf' to kickflip 'hf' to heelflip 'bssh' backside shuv 'fssh' frontside shuv 'tre' to treflip 'exit' to exit"]
odds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
game_active = True
health = (8)
SKATE = []
skateFull = ['S', 'K', 'A', 'T', 'E']
lineBonus = (0)

name = input("What is your name? ")

print(Fore.WHITE + 'welcome to the game of Skate')
print(name, 's score: ', SKATE)
print(Fore.CYAN, trickList)

while game_active == True:
    sleep(.5)
    currentTrick = random.choice(trickList)
    print(Fore.CYAN  + 'CPU did a' , currentTrick)
    print(Fore.WHITE + 'enter trick:')

    trickSelection = str.lower(input(Fore.YELLOW))


 

    if trickSelection == 'ol' and currentTrick == 'ol':
        if random.choice(odds) >= 30:
            print(Fore.GREEN + 'OLLIE 🛹')
            lineBonus = lineBonus + 1
            print(Fore.WHITE + 'you have', lineBonus, 'line bonus')
        else:
            print(Fore.RED + 'slipped and hit your head')
            health = health - 1
            print(Fore.RED, health, '❣️')
            lineBonus = 0
            if SKATE == []:
                SKATE.append('S')
                print(SKATE)
            elif SKATE == ['S']:
                SKATE.append('K')
                print(SKATE)
            elif SKATE == ['S', 'K']:
                SKATE.append('A')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A']:
                SKATE.append('T')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A', 'T']:
                SKATE.append('E')
                print(SKATE)
                print('GAME OVER ☠️')
                game_active = False
            
       


    if trickSelection == 'kf':
        if random.choice(odds) >= 50:
            print(Fore.GREEN + 'KICKFLIP 🛹')
            lineBonus = lineBonus + 1
            print(Fore.WHITE + 'you have', lineBonus, 'line bonus')
   
        else:
            print(Fore.RED + 'landed on truck and rolled ankle')
            health = health - 1
            print(health, '❣️')
            lineBonus = 0
            if SKATE == []:
                SKATE.append('S')
                print(SKATE)
            elif SKATE == ['S']:
                SKATE.append('K')
                print(SKATE)
            elif SKATE == ['S', 'K']:
                SKATE.append('A')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A']:
                SKATE.append('T')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A', 'T']:
                SKATE.append('E')
                print(SKATE)
                print('GAME OVER ☠️')
                game_active = False
            

    if trickSelection == 'hf':
        if random.choice(odds) >= 60:
            print(Fore.GREEN + 'HEELFLIP 🛹')
            lineBonus = lineBonus + 1
            print(Fore.WHITE + 'you have', lineBonus, 'line bonus')
   
        else:
            print(Fore.RED + 'Creditcard!!!') 
            health = health - 1
            print(health, '❣️')
            lineBonus = 0
            if SKATE == []:
                SKATE.append('S')
                print(SKATE)
            elif SKATE == ['S']:
                SKATE.append('K')
                print(SKATE)
            elif SKATE == ['S', 'K']:
                SKATE.append('A')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A']:
                SKATE.append('T')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A', 'T']:
                SKATE.append('E')
                print(SKATE)
                print('GAME OVER ☠️')
                game_active = False

    if trickSelection == 'bssh':
        if random.choice(odds) >= 40:
            print(Fore.GREEN + 'Shuvit 🛹')
            lineBonus = lineBonus + 1
            print(Fore.WHITE + 'you have', lineBonus, 'line bonus')
    
        else:
            print(Fore.RED + 'shinner!')
            health = health - 1
            print(health, '❣️')
            lineBonus = 0
            if SKATE == []:
                SKATE.append('S')
                print(SKATE)
            elif SKATE == ['S']:
                SKATE.append('K')
                print(SKATE)
            elif SKATE == ['S', 'K']:
                SKATE.append('A')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A']:
                SKATE.append('T')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A', 'T']:
                SKATE.append('E')
                print(SKATE)
                print('GAME OVER ☠️')
                game_active = False

    if trickSelection == 'fssh':
        if random.choice(odds) >= 50:
            print(Fore.GREEN + 'Front Shuvit 🛹')
            lineBonus = lineBonus + 1
            print(Fore.WHITE + 'you have', lineBonus, 'line bonus')
    
        else:
            print(Fore.RED + 'landed on toe!')  
            health = health - 1
            print(health, '❣️')      
            lineBonus = 0
            if SKATE == []:
                SKATE.append('S')
                print(SKATE)
            elif SKATE == ['S']:
                SKATE.append('K')
                print(SKATE)
            elif SKATE == ['S', 'K']:
                SKATE.append('A')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A']:
                SKATE.append('T')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A', 'T']:
                SKATE.append('E')
                print(SKATE)
                print('GAME OVER ☠️')
                game_active = False

    if trickSelection == 'tre':
        if random.choice(odds) >= 75: 
            print(Fore.GREEN + 'Steezy tre flip 🛹')
            lineBonus = lineBonus + 1
            print(Fore.WHITE + 'you have', lineBonus, 'line bonus')
    
        else:
            print(Fore.RED + 'not even close')
            health = health - 1
            print(health, '❣️')
            lineBonus = 0
            if SKATE == []:
                SKATE.append('S')
                print(SKATE)
            elif SKATE == ['S']:
                SKATE.append('K')
                print(SKATE)
            elif SKATE == ['S', 'K']:
                SKATE.append('A')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A']:
                SKATE.append('T')
                print(SKATE)
            elif SKATE == ['S', 'K', 'A', 'T']:
                SKATE.append('E')
                print(SKATE)
                print('GAME OVER ☠️')
                game_active = False

    if trickSelection == 'list':
        print(Fore.CYAN, trickList)

    if health == 0:
        print(Fore.RED + 'you died ☠️')
        game_active = False
        print(Fore.RED + 'game over')

    if lineBonus == 3:
        health = health + 1
        print(Fore.GREEN + 'you got a line bonus + 1 health ❣️ ', health)    
        lineBonus = 0

    if trickSelection == 'exit':
        game_active = False
        print('goodbye')