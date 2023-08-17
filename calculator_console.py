from  colorama  import  init
from  colorama  import  Fore ,  Back ,  Style 
init ()

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("Calcu.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()

print ( Fore.BLACK )
print ( Back.YELLOW )

what = input ("Что делать (+,-,*,/, **):")

print ( Back.MAGENTA )

a = float (input("Введите первое число:"))
b = float (input("Введите второе число:"))

print ( Back.CYAN )

if what == "+":
    c = a + b
    print ("Ответ:" + str(c))
elif what == "-":
    c = a - b
    print ("Ответ:" + str(c))
elif what == "*":
    c = a * b
    print ("Ответ:" + str(c))
elif what == "/":
    c = a / b
    print ("Ответ:" + str(c))
elif what == "**":
    c = a ** b
    print ("Ответ:" + str(c))
else:
    print ("Ты бездарная свинья, у тебя ошибка в знаках!")
input ()