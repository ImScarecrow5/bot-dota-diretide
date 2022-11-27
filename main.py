from PIL import ImageGrab
import tkinter
import numpy as np
import time
import cv2
import pyautogui

class Diretide:
    def __init__(self):
        self.root = tkinter.Tk()
        self.width1 = self.root.winfo_screenwidth()
        self.height1 = self.root.winfo_screenheight()
        print(self.width1, 'x', self.height1, sep='')

        self.template = cv2.imread('screenshot/go.png', 0)  # читаем картинку
        self.w, self.h = self.template.shape[::-1]  # высота и ширина скриншота

        self.photo2 = cv2.imread('screenshot/agree.png', 0)  # читаем картинку
        self.w2, self.h2 = self.photo2.shape[::-1]  # высота и ширина скриншота

        self.resume1 = cv2.imread('screenshot/resume.png', 0)  # читаем картинку
        self.w3, self.h3 = self.resume1.shape[::-1]  # высота и ширина скриншота

        self.hero1 = cv2.imread('screenshot/hero.png', 0)  # читаем картинку
        self.w4, self.h4 = self.hero1.shape[::-1]  # высота и ширина скриншота

        print('Запуск через:')
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)

    def found_agree(self):
        self.flag = True
        while self.flag:  # Пытаемся найти поиск
            print('not found agree game')
            self.screen_base = ImageGrab.grab(bbox=(0, 0, self.width1, self.height1))  # resolution
            self.screen_base.save('screenshot/base_screen.png')

            self.img_rgb2 = cv2.imread('screenshot/base_screen.png')  # Конвертируем пнг для opencv
            self.img_gray2 = cv2.cvtColor(self.img_rgb2, cv2.COLOR_BGR2GRAY)  # чтобы быстрее искалось

            self.res2 = cv2.matchTemplate(self.img_gray2, self.photo2, cv2.TM_CCOEFF_NORMED)  # поиск
            self.loc2 = np.where(self.res2 >= 0.9)  # координаты

            for pt in zip(*self.loc2[::-1]):
                self.x = int(pt[0])
                self.y = int(pt[1])
                self.agree_screen = ImageGrab.grab(bbox=(self.x, self.y, self.x + self.w2, self.y + self.h2))
                self.agree_screen.save('screenshot/agree_screen.png')
                print('found agree game!')  # Приняли игру
                pyautogui.moveTo(self.x + 10, self.y + 5)
                pyautogui.mouseUp()
                time.sleep(0.4)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(0.2)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(0.2)
                pyautogui.mouseDown()
                self.flag = False
                self.hero()

    def hero(self):
        print('not found hero')
        self.screen_base = ImageGrab.grab(bbox=(0, 0, self.width1, self.height1))  # resolution
        self.screen_base.save('D:/pythonptoject/test/screenshot/base_screen.png')

        self.img_rgb5 = cv2.imread('screenshot/base_screen.png')  # Конвертируем пнг для opencv
        self.img_gray5 = cv2.cvtColor(self.img_rgb5, cv2.COLOR_BGR2GRAY)  # чтобы быстрее искалось

        self.res5 = cv2.matchTemplate(self.img_gray5, self.hero1, cv2.TM_CCOEFF_NORMED)  # поиск
        self.loc5 = np.where(self.res5 >= 0.9)  # координаты

        for pt in zip(*self.loc5[::-1]):
            self.x = int(pt[0])
            self.y = int(pt[1])
            self.start_screen = ImageGrab.grab(bbox=(self.x, self.y, self.x + self.w4, self.y + self.h4))
            self.start_screen.save('screenshot/hero_screen.png')
            print('found hero!')
            pyautogui.moveTo(self.x + 10, self.y + 5)
            pyautogui.mouseUp()
            time.sleep(0.4)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(0.2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(0.2)
            pyautogui.mouseDown()
            print('click on hero')  # Нажали на героя
            # self.found_resume()
            self.flag = False

    def found_start(self):
        self.flag = True
        while self.flag:  # Пытаемся найти игру
            print('not found start game')
            self.screen_base = ImageGrab.grab(bbox=(0, 0, self.width1, self.height1))  # resolution
            self.screen_base.save('D:/pythonptoject/test/screenshot/base_screen.png')

            self.img_rgb = cv2.imread('screenshot/base_screen.png')  # Конвертируем пнг для opencv
            self.img_gray = cv2.cvtColor(self.img_rgb, cv2.COLOR_BGR2GRAY)  # чтобы быстрее искалось

            self.res = cv2.matchTemplate(self.img_gray, self.template, cv2.TM_CCOEFF_NORMED)  # поиск
            self.loc = np.where(self.res >= 0.9)  # координаты

            for pt in zip(*self.loc[::-1]):
                self.x = int(pt[0])
                self.y = int(pt[1])
                self.start_screen = ImageGrab.grab(bbox=(self.x, self.y, self.x + self.w, self.y + self.h))
                self.start_screen.save('screenshot/start_screen.png')
                print('found start game!')
                pyautogui.moveTo(self.x + 10, self.y + 5)
                pyautogui.mouseUp()
                time.sleep(0.4)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(0.2)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(0.2)
                pyautogui.mouseDown()
                print('click start game')  # Запустили поиск
                self.found_agree()
                self.flag = False

    def found_resume(self):
        self.flag = True
        while self.flag:  # Пытаемся найти игру
            print('not found resume game')
            self.screen_base = ImageGrab.grab(bbox=(0, 0, self.width1, self.height1))  # resolution
            self.screen_base.save('D:/pythonptoject/test/screenshot/base_screen.png')

            self.img_rgb3 = cv2.imread('screenshot/base_screen.png')  # Конвертируем пнг для opencv
            self.img_gray3 = cv2.cvtColor(self.img_rgb3, cv2.COLOR_BGR2GRAY)  # чтобы быстрее искалось

            self.res3 = cv2.matchTemplate(self.img_gray3, self.resume1, cv2.TM_CCOEFF_NORMED)  # поиск
            self.loc3 = np.where(self.res3 >= 0.9)  # координаты

            for pt in zip(*self.loc3[::-1]):
                self.x = int(pt[0])
                self.y = int(pt[1])
                self.start_screen = ImageGrab.grab(bbox=(self.x, self.y, self.x + self.w3, self.y + self.h3))
                self.start_screen.save('screenshot/resume_screen.png')
                print('found resume game!')
                pyautogui.moveTo(self.x + 10, self.y + 5)
                pyautogui.mouseUp()
                time.sleep(0.4)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(0.2)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(0.2)
                pyautogui.mouseDown()
                print('click resume game')  # Нажали продолжить
#                self.found_start()
                self.flag = False


if __name__ == '__main__':
    pt = Diretide()
    pt.hero()