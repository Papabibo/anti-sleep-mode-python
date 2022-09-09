import pyautogui
import time

while True:
    pyautogui.moveRel(0, 1)
    time.sleep(60) #secondes
    pyautogui.moveRel(0, -1)
    time.sleep(60) #secondes