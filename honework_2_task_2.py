# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

class Check_for_parity:
    '''
    Создаем класс который принимает число и определяет количество четных и нечетных чисел.
    '''
    def __init__(self, number):
        self.number = number
        self.even_numbers = 0
        self.list_even_numbers = []
        self.odd_numbers = 0
        self.list_odd_numbers = []

    def check_parity(self):
        '''
        Создаем метод который определяет четные и нечетные цифры в числе
        '''
        for num in self.number:
            num = int(num)
            if num % 2 == 0:
                self.even_numbers += 1
                self.list_even_numbers.append(num)
            else:
                self.odd_numbers += 1
                self.list_odd_numbers.append(num)
        print(f'Данное число содержит {self.even_numbers} {self.list_even_numbers} четных цифр и {self.odd_numbers} {self.list_odd_numbers} нечетных цифр')

number = input('Введите число которое ходите проверить на четность цифр составляющих его: ')

Check_for_parity(number).check_parity()
