import time

import pyautogui

while True:
    time.sleep(5)
    pyautogui.typewrite("Hello! How can I help you?")
    time.sleep(2)
    pyautogui.press("enter")