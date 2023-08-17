from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
from PIL import Image, ImageTk

def btn_click_more():
	global money_label
	global money
	global number
	global number_label
	global number2
	global number2_label
	number = random.randint(1, 100)
	number_label = Label(frame, text=number, bg='pink', font=50)
	number_label.place(relx=0.25, rely=0.3, relwidth=0.15, relheight=0.15)
	number2 = random.randint(1, 100)
	number2_label = Label(frame, text=number2, bg='pink', font=50)
	number2_label.place(relx=0.60, rely=0.3, relwidth=0.15, relheight=0.15)
	money_label = Label(frame, text=money, bg='yellow', font=50)
	money_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.2)
	if number >= number2:
		money += 500
		number_2 = random.randint(1, 100)
	else:
		money -=500
		number_2 = random.randint(1, 100)

def btn_click_equal():
	global money_label
	global money
	global number
	global number_label
	global number2
	global number2_label
	number = random.randint(1, 100)
	number_label = Label(frame, text=number, bg='pink', font=50)
	number_label.place(relx=0.25, rely=0.3, relwidth=0.15, relheight=0.15)
	number2 = random.randint(1, 100)
	number2_label = Label(frame, text=number2, bg='pink', font=50)
	number2_label.place(relx=0.60, rely=0.3, relwidth=0.15, relheight=0.15)
	money_label = Label(frame, text=money, bg='yellow', font=50)
	money_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.2)
	if number == number2:
		money += 1000
		number_2 = random.randint(1, 100)
	else:
		money -=500
		number_2 = random.randint(1, 100)

def btn_click_less():
	global money_label
	global money
	global number
	global number_label
	global number2
	global number2_label
	number = random.randint(1, 100)
	number_label = Label(frame, text=number, bg='pink', font=50)
	number_label.place(relx=0.25, rely=0.3, relwidth=0.15, relheight=0.15)
	number2 = random.randint(1, 100)
	number2_label = Label(frame, text=number2, bg='pink', font=50)
	number2_label.place(relx=0.60, rely=0.3, relwidth=0.15, relheight=0.15)
	money_label = Label(frame, text=money, bg='yellow', font=50)
	money_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.2)
	if number <= number2:
		money += 500
		number_2 = random.randint(1, 100)
	else:
		money -=500
		number_2 = random.randint(1, 100)

#Start program
root = Tk()
root['bg'] = '#fff'

# root.wn_attributes("-tompost", 1)

root.title('Casino') #Name of program
root.geometry('500x500') #Size of program



frame = Frame(root)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

path = 'Casino.png'

image = Image.open(path)
width = 500
ratio = (width / float(image.size[0]))
height = int((float(image.size[1]) * float(ratio)))
image = image.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

frame = tk.Canvas(root, width=width, height=height)
frame.pack(side="top", fill="both", expand="no")

frame.create_image(0, 0, anchor="nw", image=image)

# image1 = PhotoImage(file = "Casino.png")
# image1_label = Label(root)
# image1_label.image = image1
# image1_label['image'] = image1_label.image
# image1_label.place(x = 0, y = 0)

money = 1000
money_label = Label(frame, text=money, bg='yellow')
money_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.2)

btn1 = Button(frame, text='Больше', bg='green', command=btn_click_more)
btn1.place(relx=0.25, rely=0.1)


btn2 = Button(frame, text='Равно', bg='green', command=btn_click_equal)
btn2.place(relx=0.45, rely=0.1)


btn3 = Button(frame, text='Меньше', bg='green', command=btn_click_less)
btn3.place(relx=0.63, rely=0.1)

root.mainloop() #Start infinity program. WRITE ALWAYS