import webbrowser as wb
import pyautogui as pg
import datetime
import os
import random as rd
import pyglet

class Function:
    def playMusic(self):
        song_run = pyglet.media.load('musics\simple' + str(rd.randint(1, 10)) + '.mp3')
        song_run.play()
        pyglet.app.run()

    def playPhonk(self):
        song_run = pyglet.media.load('musics\phonk' + str(rd.randint(1, 9)) + '.mp3')
        song_run.play()
        pyglet.app.run()

    def offPc(self):
        os.system("shutdown -s")

    def openBrowse(self):
        wb.open("https://www.google.com/")

    def takeScreenshot(self):
        pg.screenshot("photo.png")

    def timeNow(self):
        now = datetime.datetime.now()
        time_now = "Сейчас {}:{}".format(str(now.hour), str(now.minute))

    def openTelegram(self):
        os.startfile(r'C:\Users\Администратор\AppData\Roaming\Telegram Desktop\Telegram.exe')
