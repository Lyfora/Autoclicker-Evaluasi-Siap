import pyautogui
import time

# Must Read
# This code only works if you already install pyautogui
# ! If you don't have, you can go to terminal and write this command 'pip install pyautogui'
# !! After you run this code, don't forget to click the browser again, coz this command run locally in your computer!
# Initialize!
time.sleep(2)
pyautogui.scroll(1920)

# x is initialize how much Lecturer that you want to evaluate!
# As an example, i set 5 as default
for x in range(1):
    # Clicking the bar
    pyautogui.moveTo(920, 380)
    time.sleep(1)
    pyautogui.leftClick()
    if (x == 0):
        pyautogui.press('enter')
    else:
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
    time.sleep(2)
    for y in range(34):
        pyautogui.press('tab')
        pyautogui.press('space')
    time.sleep(1)
    pyautogui.scroll(-1920)
    pyautogui.moveTo(950, 820)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.scroll(1920)
