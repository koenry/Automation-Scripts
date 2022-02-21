import pyautogui
import time
import cv2
import subprocess
import webbrowser
from PIL import ImageGrab, Image

def main(): 
    time.sleep(2)
    image = pyautogui.locateOnScreen("1.png")
    while image == None:
        image = pyautogui.locateOnScreen('1.png', confidence=.5) # wait for browser to load
        time.sleep(2)
        print("Still loading")
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('1.png', confidence=.5))

    # Wait for login screen to appear
    image = pyautogui.locateOnScreen("login.png")
    while image == None:
        image = pyautogui.locateOnScreen('login.png', confidence=.5)
        time.sleep(1)
        print("Still loading")
        
    # log in
    time.sleep(1)
    pyautogui.typewrite('user')
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite('pass')
    time.sleep(0.5)
    pyautogui.press('enter')

# locate tab
    time.sleep(1.5)
    image = pyautogui.locateOnScreen("2.png")
    while image == None:
        image = pyautogui.locateOnScreen('2.png', confidence=.7)
        time.sleep(2)
        print("Still loading")
    pyautogui.click(pyautogui.locateCenterOnScreen('2.png', confidence=.7))

    time.sleep(1.5)
    pyautogui.press('tab', presses=5) # Tab to the correct... Tab
    time.sleep(1)
    pyautogui.press('enter') # Confirm 
    time.sleep(1)
   
    pyautogui.click(x=711, y=422)
    time.sleep(2)
    pyautogui.scroll(-30000)  # scroll to the end
    time.sleep(1)
    pyautogui.scroll(-30000)
    time.sleep(1)
    pyautogui.scroll(-30000) 
    time.sleep(1)
    

###############################1st WEB#################################
    
webbrowser.open('https://IP/') 
main()
time.sleep(1.5)
im = ImageGrab.grab(bbox=(15,135,1280,770)) # coordinates of what to screenshot. Coordinates differ from one screen res to another
im.save("output/1.jpg")
time.sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen('logout.png', confidence=.5))
time.sleep(2)















