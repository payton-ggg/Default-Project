import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

# Создание приложения
app = tk.Tk()
app.title("Поисковая система")

# Создание текстовой надписи
search_label = ttk.Label(app, text='Поиск')
search_label.grid(row=0, column=0)

# Создание поля для ввода информации
text_field = ttk.Entry(app, width=50)
text_field.grid(row=0, column=1)

search_engine = StringVar()
search_engine.set("google")

# Поиск информации в Интернете
def search():
    if text_field.get().strip() != "":
        if search_engine.get() == "google":
            webbrowser.open('https://www.google.com/search?q=' + text_field.get())
        elif search_engine.get() == "yandex":
            webbrowser.open('https://music.youtube.com/search?q='+ text_field.get())

def searchBtn():
    search()

def enterBtn(event):
    search()



# Кнопка поиска
btn_search = ttk.Button(app, text='Найти', width=10, command=searchBtn)
btn_search.grid(row=0, column=2)

# Отслеживание события нажатия на клавишу Enter
text_field.bind('<Return>', enterBtn)

radio_google = ttk.Radiobutton(app, text='Google', value='google', variable=search_engine)
radio_google.grid(row=1, column=1, sticky=W)

radio_yandex = ttk.Radiobutton(app, text='Youtube Music', value='yandex', variable=search_engine)
radio_yandex.grid(row=1, column=1, sticky=E)

app.wm_attributes('-topmost', True)

text_field.focus()

# Функция, позволяющая не закрывать приложение
app.mainloop()
