import pyautogui
import time
import subprocess
import cv2
import os
import datetime
from PIL import ImageGrab, Image

# we're using alt+prtscrn to take a ss of the current window and PIL to grab from clipboard and save it

def main():
    time.sleep(1.5)
    image = pyautogui.locateOnScreen("glance1.png") # waits for putty to fully load
    while image == None:
        image = pyautogui.locateOnScreen('glance1.png', confidence=.5)
        time.sleep(1)
        print("Still loading")
    pyautogui.typewrite('glance')         # GLANCE command
    time.sleep(1)
    pyautogui.press('enter')

    image = pyautogui.locateOnScreen("glance2.png") # waits for glance to completely load
    while image == None:
        image = pyautogui.locateOnScreen('glance2.png', confidence=.5)
        time.sleep(1)
        print("Still loading")
    pyautogui.press('q')
    time.sleep(1)

def end():
    time.sleep(0.5)
    pyautogui.typewrite('exit')  # double exit for CMD to putty on w7
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.typewrite('exit')  # double exit for CMD to putty on w7
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)


# Server1

time.sleep(1)
subprocess.Popen("putty.exe user@IP -pw PASSWORD")
time.sleep(1.5)
main()
pyautogui.hotkey('alt', 'PrtSc')
im = ImageGrab.grabclipboard()
if isinstance(im, Image.Image):
    im.save('output/1.jpg')
end()

# vice-versa for all other servers left

print("************************************FINISHED***********************************\n")
raw_input("\nPress Enter to continue...")

