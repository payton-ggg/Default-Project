from  colorama  import  init
from  colorama  import  Fore ,  Back ,  Style 
init ()

print ( Fore.BLACK )
print ( Back.YELLOW )

a = int(input("Колличество эпизодов:"))

d = (a * 21)
b = str(d / 60)

print ( Back.GREEN )

print ("В минутах:" + str(d))
print ("В часах:" + b)
input() 