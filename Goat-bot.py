import pyautogui
import cv2
import time

# the things below are variables.

a = 0
evobox = 0
berry = 0

# Goat evolution autoboxes and berries!
# maybe more soon? haven't decided yet!
# Berries = broken. fix soon?

while a == 0:
    if berry <= 45:
        cratepos = pyautogui.locateOnScreen(r"C:\Users\aGooglyBiscuit\OneDrive\goat evo\Images\Crate-Laptop.png", confidence=0.5)
        if cratepos == None:
            takebutton = pyautogui.locateOnScreen(r"C:\Users\aGooglyBiscuit\OneDrive\goat evo\Images\Take-Button-Laptop.png", confidence=0.5)
            if takebutton == None:
                None
            else:
                print("Found take button at:", takebutton)
                pyautogui.moveTo(takebutton)
                pyautogui.leftClick()
                berry += 1
        else:
            print("Found a crate at:", cratepos)
            pyautogui.moveTo(cratepos)
            pyautogui.leftClick()
            berry += 1
        if evobox >= 20:
            posevobox = pyautogui.locateOnScreen(r"C:\Users\aGooglyBiscuit\OneDrive\goat evo\Images\Evolution-Crate-Laptop.png", confidence=0.5)
            if posevobox == None:
                evobox == 0
            else:
                print("Found an Evolution box at:", posevobox)
                pyautogui.moveTo(posevobox)
                pyautogui.leftClick()
                evobox == 0
        else:
            evobox += 1
    else:
        posredberry = pyautogui.locateOnScreen(r"C:\Users\aGooglyBiscuit\OneDrive\goat evo\Images\Poopy-Berry-Laptop.png", confidence=0.5)
        if posredberry == None:
            posblueberry = pyautogui.locateOnScreen(r"C:\Users\aGooglyBiscuit\OneDrive\goat evo\Images\Diamond-Berry-Laptop.png", confidence=0.5)
            if posblueberry == None:
                posyellowberry = pyautogui.locateOnScreen(r"C:\Users\aGooglyBiscuit\OneDrive\goat evo\Images\Combine-Berry-Laptop.png", confidence=0.5)
                if posyellowberry == None:
                    None
                else:
                    pyautogui.moveTo(posyellowberry)
                    pyautogui.leftClick()
                    print("Clicked on a Yellow berry!")
                    berry == 0
            else:
                pyautogui.moveTo(posblueberry)
                pyautogui.leftClick()
                print("Clicked on a Blue berry!")
                berry == 0
        else:
            pyautogui.moveTo(posredberry)
            pyautogui.leftClick()
            print("Clicked on a Red berry!")
            berry == 0
