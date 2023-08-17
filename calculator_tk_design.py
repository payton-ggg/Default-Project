from tkinter import *

root = Tk() 

root.geometry("312x324")
# Prevent root window from been resized:

root.resizable(0, 0)
# Window title:

root.title("Calculator")

# 3a. btn_click function updates the input field whenever a number is entered. Any button pressed will act as a button click update:

def btn_click(item):
	global expression
	expression = expression + str(item)
	input_text.set(expression)
	# 3b. btn_clear function clears the input field and previous calculations using the ’Clear’ button:

def btn_clear():
	global expression
	expression = ""
	input_text.set("")
	# 3c. btn_equal function calculates the expression entered in the input field. 

def btn_equal():
    global expression
 	# eval() function evaluates the string expressions directly:   

    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
expression = ""
	# StringVar()’ is used to get the instance of the input field:

input_text = StringVar()

# 4a. Use the Frame widget to create a frame for the input field:

input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

# 4b. Create an input field inside the Frame created in the previous step. Output aligned to the  right:

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)
# ‘ipady’ is internal padding that increases the height of the input field.

 

# 4c. Create a separate Frame below the input field, which will include buttons positioned in rows inside the frame:

btns_frame = Frame(root, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()
# The remainder of this section defines Button widgets arranged in 5 rows within a Frame widget. The buttons are positioned using the grid() Layout Manager. Each Button has an event that can be triggered with a mouse action configured in the previous section. E.g. btn_click()

 

# 4d. First row includes 2 buttons, ‘Clear (Clear)’ and ‘Divide (/)’: 

clear = Button(btns_frame, text = "Clear", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
# 4e. Second row includes 4 buttons, ‘7’, ‘8’, ‘9’ and ‘Multiply (*)’:

seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
# 4f. Third row includes 4 buttons,  ‘4’, ‘5’, ‘6’ and ‘Subtract (-)’:

four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
# 4g. Fourth row includes 4 buttons, ’1’, ’2’, ’3’, and ’plus (+)’: 

one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
# 4h. Fifth row includes 3 buttons,  ‘0’, ‘Decimal (.)’, and ‘Equal To (=)’:

zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop() #Start infinity program. WRITE ALWAYS