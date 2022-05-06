import pyautogui
import time

frequency = 5
while frequency > 0:
    time.sleep(4)
    pyautogui.typewrite("yello! trying something")
    time.sleep(2)
    pyautogui.press("enter")
    frequency = frequency - 1

    