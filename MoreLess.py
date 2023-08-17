import random

from  colorama  import  init
from  colorama  import  Fore ,  Back ,  Style 

init ()

print ( Fore.BLACK )
print ( Back.CYAN )

print("Больше Меньше")
print('Игра "Больше Меньше" правила просты, как и само название:')
print("Для начала вам нужно сделать ставку. Минимальный размер ограничен 1 фишка, максимальный — неограничен, однако цена должна быть в пределах цены вашей почки")
print("После размещения ставки вы увидите случайное число от 1 до 100. От вас требуется угадать, будет следующее число больше, меньше или равно предыдущему")

#Твой баланс

print("Одна фишка стоит $500")

@eel.expose

def get_game(place):
	your_cash = 5000

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
	input()