import random
from  colorama  import init
from  colorama  import  Fore ,  Back ,  Style 
init ()

print ( Back.GREEN )

print("Game of thimbles")

print ( Fore.BLACK )
print ( Back.YELLOW )

#Под каким ведром напёрсток

bucket = random.randint(1, 3)

#Твой баланс

print("Одна фишка стоит $500")

your_cash = int(input("Твой баланс:"))

#Сколько у тебя фишек

your_chips = int(your_cash / 500)

print("У тебя есть:",  your_chips, "фишек")

#Проверка есть ли у тебя достаточное колличество денег

print ( Back.RED )
	#Цикл

while your_chips > 0:

	#Рандомно ставит шарик под ведро

	bucket = random.randint(1, 3)

	#Твои догадки под каким ведром шарик

	your_answer = int(input("Под каким ведром напёрсток:"))

	#Если ответ правильный выполняется следующие 

	if bucket == your_answer:

		#Прибавляется сумма к общему балансу

		your_cash += 500
		your_chips += 1
		print("Правильно", "У тебя осталось:", your_chips, "фишек")

		#Запрос на продолжение

		continue_1 = input("Хочешь ли ты продолжить (Y/N):")

		#Если продолжишь то выполняется идентичное тому чтот сверху

		if continue_1 == "Y": continue 
			# bucket = random.randint(1, 3)
			# your_answer = int(input("Под каким ведром напёрсток:"))
			# if bucket == your_answer:
			# 	your_cash += 500
			# 	print("Right!", "Твой баланс:", your_cash)

			# 	#Если ответ не верный

			# else:
			# 	your_cash += -500
			# 	print("Бездарь, не правильно, правильный ответ:", bucket)
		else:
			print("У тебя осталось:", your_chips, "фишек")
			break
	
	#Если на 28 строчке ответишь не правильно происходит ряд идентичных действий 
	
	else:
		your_cash -= 500
		your_chips -= 1
		print("Бездарь, не правильно, правильный ответ:", bucket)
		print("У тебя осталось:", your_chips, "фишек")
		continue_2 = input("Хочешь ли ты продолжить (Y/N):")
		if continue_2 == "Y": continue
			# bucket = random.randint(1, 3)
			# your_answer = int(input("Под каким ведром напёрсток:"))
			# if bucket == your_answer:
			# 	your_cash += 500
			# 	print("Right!", "Твой баланс:", your_cash)
			# 	continue_1 = input("Хочешь ли ты продолжить (Y/N):")
			# else:
			# 	your_cash += -500
			# 	print("Бездарь, не правильно, правильный ответ:", bucket)
		else:
			print("У тебя осталось:", your_chips, "фишек")
			break

#Если твоих денег не достаточно то выполниться это

else:
	print("Бездарь, у тебя не хватает денег. Вали отсюда, бомж")

print ( Back.WHITE )

if your_cash < 0:
	print("У тебя есть", your_chips , "фишек." "Или же", your_cash, "$")
	print("Ты должен казино.", "Завтра денег не будет, я тебя вскрою, почку заберу и мы будем в расчёте")
else:
	print("У тебя есть", your_chips , "фишек." "Или же", your_cash, "$")
	print("Не знаю как тебе удaлось не обанкротится в казино, но больше не возвращайся сюда, с надеждой выиграть")
input()