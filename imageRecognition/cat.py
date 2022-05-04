
import pyautogui
from pyautogui import *
import time from sleep
import keyboard
import random
import win32api, win32con


while 1:
    if pyautogui.locateOnScreen('catPy.png') != None:
        print("I Can see the cat")
        sleep(.5)
    else:
        print("Where is the cat")
        sleep(.5)
