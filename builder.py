from time import sleep

sleep(1)


myBoard = ['deck: ', 'tba', 'wheels: ', 'tba', 'bearings: ', 'tba', 'griptape: ', 'tba', 'hardware: ', 'tba', 'trucks: ', 'tba']
decks = ['girl', 'baker', 'krooked', 'real', 'enjoi']
wheels = ['spitfire', 'bones', 'sml']
bearings = ['bones', 'bronson', 'dirty bearings']
griptape = ['mob', 'miles', 'jessup']
trucks = ['indy', 'ace', 'thunder']
hardware = ['hardies', 'diamond']

print('hello skater')
confirm = str.lower(input("Want to build a skateboard? ('Y', 'N')"))

if confirm == 'y':
    print('awesome')
    sleep(2)
    print('First lets choose a deck')
    sleep(1)
    print('Here are the decks:', decks)
    sleep(1)
    myBoard[1] = str.lower(input('type the deck you want '))

    sleep(1)
    print('Last lets choose your trucks ', trucks)
    sleep(1)
    myBoard[11] = str.lower(input('type the trucks you want '))

    sleep(1)
    print('Now lets choose your wheels ', wheels)
    sleep(1)
    myBoard[3] = str.lower(input('type the wheels you want '))

    sleep(1)
    print('Now lets choose your bearings ', bearings)
    sleep(1)
    myBoard[5] = str.lower(input('type the bearings you want '))

    sleep(1)
    print('Now lets choose your griptape ', griptape)
    sleep(1)
    myBoard[7] = str.lower(input('type the griptape you want '))

    sleep(1)
    print('Now lets choose your hardware ', hardware)
    sleep(1)
    myBoard[9] = str.lower(input('type the hardware you want '))

    sleep(1)
    print('your brand new skateboard! ', myBoard)
    sleep(1)
    print('thanks for building with us!')
    sleep(1)
    print('goodbye')
else:
    print('okay, bye')
