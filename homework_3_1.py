# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

class Multiplicit_numbers:
    def __init__(self):
        self.list_numbers = {i for i in range(2, 100)}
        self.natural_numbers = {2: 0, 3: 0, 4: 0, 5:  0, 6: 0, 7:  0, 8: 0, 9: 0}

    def calculating_multiplicity(self):
        for num in self.list_numbers:
            for mul in range(2, 10):
                if num % mul == 0:
                    self.natural_numbers[mul] = self.natural_numbers[mul] + 1
        print(f'Даннные цифры кратные следующее колличество чисел {self.natural_numbers}')

num = Multiplicit_numbers()
num.calculating_multiplicity()