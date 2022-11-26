from PIL import ImageGrab
import tkinter
import numpy as np
import time
import cv2
import pyautogui

root = tkinter.Tk()
width1 = root.winfo_screenwidth()
height1 = root.winfo_screenheight()
print(width1, height1)

template = cv2.imread('screenshot/go.png', 0)  # читаем картинку
w, h = template.shape[::-1]  # высота и ширина скриншота

photo2 = cv2.imread('screenshot/agree.png', 0)  # читаем картинку
w2, h2 = photo2.shape[::-1]  # высота и ширина скриншота

print('1')
time.sleep(1)
print('2')
time.sleep(1)
print('3')
time.sleep(1)


flag = True
while flag:  # Пытаемся найти игру
    print('not found start game')
    screen_base = ImageGrab.grab(bbox=(0, 0, width1, height1))  # resolution
    screen_base.save('D:/pythonptoject/test/screenshot/base_screen.png')

    img_rgb = cv2.imread('screenshot/base_screen.png')  # Конвертируем пнг для opencv
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # чтобы быстрее искалось

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)  # поиск
    loc = np.where(res >= 0.9)  # координаты

    for pt in zip(*loc[::-1]):
        x = int(pt[0])
        y = int(pt[1])
        start_screen = ImageGrab.grab(bbox=(x, y, x + w, y + h))
        start_screen.save('screenshot/start_screen.png')
        print('found start game!')
        pyautogui.moveTo(x + 10, y + 5)
        pyautogui.mouseUp()
        time.sleep(0.4)
        pyautogui.mouseUp()
        time.sleep(0.2)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(0.2)
        pyautogui.mouseDown()
        pyautogui.moveTo(x + 210, y + 15)
        time.sleep(2)
        pyautogui.mouseUp()
        time.sleep(0.2)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(0.2)
        pyautogui.mouseDown()
        print('click start game')  # Запустили поиск
        flag = False


flag2 = True
while flag2:  # Пытаемся найти поиск
    print('not found start game')
    screen_base = ImageGrab.grab(bbox=(0, 0, width1, height1))  # resolution
    screen_base.save('screenshot/base_screen.png')

    img_rgb2 = cv2.imread('screenshot/base_screen.png')  # Конвертируем пнг для opencv
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)  # чтобы быстрее искалось

    res2 = cv2.matchTemplate(img_gray2, photo2, cv2.TM_CCOEFF_NORMED)  # поиск
    loc2 = np.where(res2 >= 0.9)  # координаты

    for pt in zip(*loc2[::-1]):
        x = int(pt[0])
        y = int(pt[1])
        agree_screen = ImageGrab.grab(bbox=(x, y, x + w2, y + h2))
        agree_screen.save('screenshot/agree_screen.png')
        print('found agree game!')  # Приняли игру
        pyautogui.moveTo(x + 10, y + 5)
        flag2 = False