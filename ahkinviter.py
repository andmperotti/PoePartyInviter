import keyboard
import time
import pygetwindow as gw

NamesFile = 'names.txt'
daBois = []
poeWindow = gw.getWindowsWithTitle('Path of Exile')[0]

with open(NamesFile, encoding = 'utf-8') as f:
    for line in f:
        daBois.append(line.rstrip())
        
def inviter():
    time.sleep(0.1)
    poeWindow.activate()
    time.sleep(0.1)
    keyboard.press_and_release('escape')
    keyboard.press_and_release('space')
    for person in daBois:
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        keyboard.write(f"/invite {person}")
        keyboard.press_and_release('enter')
        time.sleep(0.1)

inviter()