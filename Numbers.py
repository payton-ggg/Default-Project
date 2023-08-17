import random
from  colorama  import  init
from  colorama  import  Fore ,  Back ,  Style
init()
 
print ( Fore.BLACK )
print ( Back.GREEN )

print("Game of Numbers")
print("Суть игры заключается в том, что. Генерируется 3 числа, если два из них одинаковы вы получаете определённую сумму")

print("Одна фишка стоит $500")

your_cash = float(input("Твой баланс:"))

#Сколько у тебя фишек

your_chips = float(your_cash / 500)

print("У тебя есть:",  your_chips, "фишек")

print ( Back.MAGENTA )

while your_chips > 0:
	one_number = random.randint(1, 7)
	two_number = random.randint(1, 7)
	three_number = random.randint(1, 7)

	continue_1 = input("Игра началась, хочешь ли ты продолжить(Y/N):")

	if continue_1 == "Y":
		print("Первое число:", one_number, "Второе число:", two_number, "Третье число:",  three_number)

		if one_number == two_number:

			your_cash += 500
			your_chips += 1

			print("Правильно!", "У тебя есть:",  your_chips, "фишек")

			continue

		elif three_number == one_number:

			your_cash += 500
			your_chips += 1

			print("Правильно!", "У тебя есть:",  your_chips, "фишек")

			continue	

		elif two_number == three_number:

			your_cash += 500
			your_chips += 1

			print("Правильно!", "У тебя есть:",  your_chips, "фишек")

			continue

		else:

			your_cash -= 500
			your_chips -= 1

			print("Нету ни единого схожего числа!", "У тебя есть:",  your_chips, "фишек")

			continue 
	else:
		break

if your_cash < 0:
	print("У тебя есть", your_chips , "фишек." "Или же", your_cash, "$")
	print("Ты должен казино.", "Завтра денег не будет, я тебя вскрою, почку заберу и мы будем в расчёте")
else:
	print("У тебя есть", your_chips , "фишек." "Или же", your_cash, "$")
	print("Не знаю как тебе удaлось не обанкротится в казино, но больше не возвращайся сюда, с надеждой выиграть")
input()