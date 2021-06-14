# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

class Sorted_int:
    def __init__(self, number):
        self.number = number

    def int_sorted(self):
        reverse_number = self.number[::-1]
        print(reverse_number)

number = input('Введите число которое хотите перевернуть. ')

Sorted_int(number).int_sorted()