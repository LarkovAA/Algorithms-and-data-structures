#  В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
#  После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
#  Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

class Quessing_game:

    def gameplay(self):
        the_hidden_number = random.randint(0, 100)
        print('Отгадайте число от 0 до 100')
        iteration_counter = 1
        while True:
            if iteration_counter == 10:
                print('Вы угадали потратили все попытки')
                break
            answer = int(input('Введите число которое считаете правильным '))
            if answer == the_hidden_number:
                print('Вы угадали')
                break
            elif answer > the_hidden_number:
                print('Вы ввели большое число')
                iteration_counter += 1
            else:
                print('Вы ввели меньшее число')
                iteration_counter += 1

Quessing_game().gameplay()