import pyautogui
import time


def main():
    time.sleep(2)                    
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(0.5)
    # sometimes a dwg file might show a printer error
    if (pyautogui.locateOnScreen('dwgerror.PNG', confidence=.6) is not None): 
        pyautogui.press('enter')
    else:
        time.sleep(1)
    """
    All of the coordinates must be found individually for a new machine because of screen resolution difference.
    You can instead use tab press = 31 times and enter for  #1
    Same goes for #2 or use tab 18 times and enter
    """
    time.sleep(0.4)
    pyautogui.click(x=740, y=268) #1
    time.sleep(0.2)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.click(x=768, y=651)       #2
    time.sleep(0.5)
    pyautogui.scroll(-1, x=1053, y=535) # center scroll    not needed but basic qol for me because easier to find the corners when zoomed out. If you want to zoom in not out change "-1" to "1"
    """
    center scroll, not needed but basic qol - easier to find the corners when zoomed out.
    """
    # the script now waits until you manually select the plot window.
    
    image = pyautogui.locateOnScreen("dwg2.png")
    while image == None:
        image = pyautogui.locateOnScreen('dwg2.png', confidence=.8)
        time.sleep(0.5)
        print("still haven't found the image")
    print('DONE!')
    pyautogui.press('tab')
    pyautogui.press('enter')


     # wait until its saved
    image = pyautogui.locateOnScreen("dwg3.png")   # after saving it will open the pdf with your default pdf viewer. Use an image so it recognizes your pdf viewer. 
    while image == None:
        image = pyautogui.locateOnScreen('dwg3.png', confidence=.8)
        time.sleep(0.5)
        print("still haven't found the image")
    print('DONE!')
    
    pyautogui.press('enter')

# wait until the new pdf shows up. dwg4 should be your default pdf viewer distinguishable image so it gets recognized.
    image = pyautogui.locateOnScreen("dwg4.png")
    while image == None:
        image = pyautogui.locateOnScreen('dwg4.png', confidence=.8)
        time.sleep(0.5)
        print("still haven't found the image")
    print('DONE!')
    
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.4)
    pyautogui.hotkey('ctrl', 'tab')

while True:
    main()



