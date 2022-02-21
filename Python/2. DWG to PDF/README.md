# dwg print to pdf
 Automates the option to print dwg files to pdf using DWG TrueView 2021


### PYAutoGUI

PyAutoGUI lets our Python script control the mouse and keyboard to automate interactions with DWG TrueView
PyAutoGUI can recognize an image on screen and click on it. While its a strong tool its a lot of trial and error.

### Who is it for?

You have 900 dwg files waiting to be printed to pdf. BUT you need to manually input the plotting size. This script automates everything and stops at the very moment you need to
select the plot window. After it saves it goes to the next tab to continue with the process. If you have the same size and properties of the dwg project file you can automate the entire process with "previous plot" This script still needs human intervention to select the plot. 

### Installing PyAutoGUI:

Install PYAutoGUI
```
Windows     py -m pip install pyautogui
```

#### Images
You need to take a screenshot of the following:

![image](https://user-images.githubusercontent.com/68077710/117440079-48403c80-af3c-11eb-9c1a-9ce7e987e8c9.png)         - First image used this may or may not appear when printing the dwgs to pdf. I had them 60 percent of the time on my batches. So the scripts runs if else. If it finds the error it presses the enter button to continue on to the next screen.
If it doesnt find it while scanning the screen it sleeps. Name it dwgerror or whatever you like but rename it on the script.

![image](https://user-images.githubusercontent.com/68077710/117439126-1e3a4a80-af3b-11eb-9da8-861c4357fd8d.png) This is the next tab which appears - the main plot screen. You may want to use a different image if it doesnt find one on your end. Name it dwg2.png.   The script waits for this menu to appear to continue running the script.

![image](https://user-images.githubusercontent.com/68077710/117440033-3b234d80-af3c-11eb-9528-f91ee9312a21.png) dwg3.png the save input like with the latter you may want to create your own for better image recognition on your end. After it finds the image it presses the enter button to save the file.

![image](https://user-images.githubusercontent.com/68077710/117440054-41192e80-af3c-11eb-9f99-105514c84464.png) dwg4.png is when the script creates a pdf and waits until your pdf viewer opens the newly created pdf file. You need an image of a certain unique screenshot of an object your pdf viewer has. Iam using sumatra pdf so I used the zoom buttons which is hard to miss or to not locate. After it finds the image it alt f4's back to trueview and ctrl+tabs to the next item you want to plot and print.

### Coordinates

You will have to find the coordinates of the plot select bar and -window button on your own. Or use the pyautogui.press tab button a certain amount of times until it rotates to the button or tab you need to click on which you will by pyautogui.press enter. Both work but after tab presses I would input a short sleep period before enter just to foolproof.

A great way to find the screen coordinates with the script provided in pyautogui docs. But if you intend to use this script or any other with pyautogui on different machines, monitors, screen resolutions its best to go for the tab and enter method. Just press tab and count how many does it take to get to the place you need to click on and press enter.
```
https://pyautogui.readthedocs.io/en/latest/mouse.html
```

### Browser Autocad

I will try to build a same app for the browser version of autocad using selenium. Iam guessing its going to be more foolproof because of the class selector which I think is miles better than image recognition and the code should be more universal across multiple machines without the need for coordinates or different images.


### End notes

One of my first real automation projects might not be perfect might not even be close to optimal but it gets the job done. Use the contents of the code to your desire by tweaking it for your own projects/ideas!
