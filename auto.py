import pyautogui as pg
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time as t

root = tk.Tk()
root.title("Управление Устройством")

root.geometry("312x324")

def takeScreen():
	i = 0

	while i < 5:
		pg.screenshot("photo" + str(i) + ".png")
		i += 1

def bomber():
	i = 0

	t.sleep(5)
	while i < 30:
		pg.write('Hello world!', interval=0.001)
		pg.typewrite(["enter"])
		i += 1

def exit():
	pg.confirm("Бажаєш покинути програму?")

btn_scrin = ttk.Button(root, text='Снимок Экрана 5 раз', width=15, command=takeScreen)
btn_scrin.grid(row=0, column=2)

btn_bomber = ttk.Button(root, text='Спам сообщений', width=17, command=bomber)
btn_bomber.grid(row=0, column=3)

btn_bomber = ttk.Button(root, text='Вопрос?', width=14, command=exit)
btn_bomber.grid(row=3, column=3)

print(pg.position())

# Функция, позволяющая не закрывать приложение
root.mainloop()
