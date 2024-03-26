
import pyautogui
import time

pyautogui.PAUSE = 0.5 
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('Enter')
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/my-drive')

pyautogui.press('Enter')

pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(1387,40)
pyautogui.mouseDown()
pyautogui.moveTo(745,359)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.hotkey('tab', 'tab', 'enter')
