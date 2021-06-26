# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections

class sixteen_number_calcul:
    def __init__(self):
        self.sixteen_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15}
        self.reverse_sixteen_number = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                               11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def calculation(self, x, action, y):
        '''
        Метод калькулятор определяет с помошью введенных параметров сумму или умножение чисел которые были введены в 16-ной системе.
        '''
        list_x = list()
        deque_list_x = collections.deque(list_x) # Создаем коллекцию deque для сохранений значений элементов х числа
        list_y = list()
        deque_list_y = collections.deque(list_y) # Создаем коллекцию deque для сохранений значений элементов y числа

        for i in x:
            num_ten = int(self.sixteen_number[i])
            deque_list_x.appendleft(num_ten) # Записываем в список переведеннее значения число х в 10-ю систему
        for i in y:
            num_ten = int(self.sixteen_number[i])
            deque_list_y.appendleft(num_ten) # Записываем в список переведеннее значения число у в 10-ю систему

        degree = 0
        num_ten_x = 0
        # Высчитываем значение х в 10-ой системе
        for i in deque_list_x:
            if degree == 0:
                num_ten_x += i
            else:
                num_ten_x += i * (16 ** degree)
            degree += 1

        degree = 0
        num_ten_y = 0
        # Высчитываем значение у в 10-ой системе
        for i in deque_list_y:
            if degree == 0:
                num_ten_y += i
            else:
                num_ten_y += i * (16 ** degree)
            degree += 1

        # Определяем какое вычисление нам нужно произвести и соответственно проводим данное действие
        if action == '+':
            number = num_ten_x + num_ten_y
        elif action == '*':
            number = num_ten_x * num_ten_y

        # В цикле переводим полученное значение из 10-ной системе в 16-ную
        list_num_sixteen = collections.deque(list())
        while True:
            if number // 16 == 0:
                list_num_sixteen.appendleft(number)
                break
            else:
                devisor = number % 16
                list_num_sixteen.appendleft(devisor)
                number = number // 16

        # Определяем из другого словаря к каким значениям относятся полученную коллекцию list_num_sixteen
        num_sixteen = []
        for i in list_num_sixteen:
            num = self.reverse_sixteen_number[i]
            num_sixteen.append(num)

        print(''.join(num_sixteen))

num = sixteen_number_calcul()

num.calculation('A2','+', 'C4F')
num.calculation('A2','*', 'C4F')