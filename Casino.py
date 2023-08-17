import random
from  colorama  import  init
from  colorama  import  Fore ,  Back ,  Style


init()

print( Back.RED )

print('Добро пожаловать в "DoubleU Casino"')

print("У нас есть игры для любого игрока, любителя, профи.")

def Thimbles():
	print ( Back.GREEN )

	print("Game of thimbles")

	print ( Fore.BLACK )
	print ( Back.YELLOW )

	#Под каким ведром напёрсток

	bucket = random.randint(1, 3)

	#Твой баланс

	print("Одна фишка стоит $500")

	your_cash = float(input("Твой баланс:"))

	#Сколько у тебя фишек

	your_chips = float(your_cash / 500)

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
def MoreLess():
	print ( Fore.BLACK )
	print ( Back.CYAN )

	print("Больше Меньше")
	print('Игра "Больше Меньше" правила просты, как и само название:')
	print("Для начала вам нужно сделать ставку. Минимальный размер ограничен 1 фишка, максимальный — неограничен, однако цена должна быть в пределах цены вашей почки")
	print("После размещения ставки вы увидите случайное число от 1 до 100. От вас требуется угадать, будет следующее число больше, меньше или равно предыдущему")

	#Твой баланс

	print("Одна фишка стоит $500")

	your_cash = float(input("Твой баланс:"))

	#Сколько у тебя фишек

	your_chips = float(your_cash / 500)

	print("У тебя есть:",  your_chips, "фишек")

	#Цикл

	print ( Back.RED )

	while True:

		#Переписывание нового числа

		#От какого числа играем

		number = random.randint(1, 100)

		#Вывод текущего числа

		print("Сейчас число равняется:" , number)

		number_2 = random.randint(1, 100)

		continue_1 = input("Хочешь ли ты продолжить (Y/N)")

		if continue_1 == "Y":
	 
			#Предугадывание числа
	 
			your_number = input("Что далее произойдёт с числом(M/L/E):")
	 		
			if your_number == "M":
				if number < number_2:
					your_cash += 500
					your_chips += 1
					print("Правильно!", "У тебя осталось:", your_chips, "фишек")
					print("Правильный ответ:", number_2)
				else:
					your_cash -= 500
					your_chips -= 1
					print("Бездарь, неправильно", "У тебя осталось:", your_chips, "фишек")
					print("Правильный ответ:", number_2)
			elif your_number == "L":
				if number > number_2:
					your_cash += 500
					your_chips += 1
					print("Правильно!", "У тебя осталось:", your_chips, "фишек")
					print("Правильный ответ:", number_2)
				else:
					your_cash += -500
					your_chips -= 1
					print("Бездарь, неправильно", "У тебя осталось:", your_chips, "фишек")
					print("Правильный ответ:", number_2)
			else:
				if number == number_2:
					your_cash += 1000
					your_chips += 2
					print("Правильно!", "У тебя осталось:", your_chips, "фишек")
					print("Правильный ответ:", number_2)
				else:
					your_cash += -500
					your_chips -= 1
					print("Бездарь, неправильно", "У тебя осталось:", your_chips, "фишек")
					print("Правильный ответ:", number_2)
		else:
			break

	if your_cash < 0:

		print("У тебя есть", your_chips , "фишек." "Или же", your_cash, "$")
		print("Ты должен казино.", "Завтра денег не будет, я тебя вскрою, почку заберу и мы будем в расчёте")

	else:

		print("У тебя есть", your_chips , "фишек." "Или же", your_cash, "$")
		print("Не знаю как тебе удaлось не обанкротится в казино, но больше не возвращайся сюда, с надеждой выиграть")

def Numbers():
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
		one_number = random.randint(1, 10)
		two_number = random.randint(1, 10)
		three_number = random.randint(1, 10)

		continue_1 = input("Игра началась, хочешь ли ты продолжить(Y/N):")
		your_bid = int(input(""))

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

while True:
	print(Back.RED)
	
	game2 = input("Хочешь ли ты продолжить играть в казино (Y/N):")

	if game2 == "Y":
		game = input("Выбери одну из игр (Напёрстки/БольшеМеньше/Числа):")

		if game == "Напёрстки":
			Thimbles()

		elif game == "БольшеМеньше":
			MoreLess()
		elif game == "Числа":
			Numbers()
		else:
			print("Неправильное написание игры")
	else:
		print("У тебя есть", your_chips , "фишек." "Или же", your_cash, "$")
		break
input()