# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import time
#print(time.time())

def number_generation(start, finish):
    number_str = str(time.time())
    number_int = time.time()
    generait = number_str.split('.')
    generait = int(generait[1])
    summ = start + finish

    while True:
        generait = generait % summ
        if generait // summ == 0 and generait > finish:
            generait = generait * number_int
        if generait // summ == 0 and generait < start:
            generait = generait * number_int
        if generait >= start and generait <= finish:
            break
    return int(generait)

start, finish = [int(i) for i in input('Введите границу чисел? ').split()]

print(number_generation(start, finish))

def float_number_generation(start, finish):
    number_int = time.time()
    generait = number_int
    summ = start + finish

    while True:
        generait = generait % summ
        if generait // summ == 0 and generait > finish:
            generait = generait * number_int
        if generait // summ == 0 and generait < start:
            generait = generait * number_int
        if generait >= start and generait <= finish:
            break
    return float(generait)

start, finish = [int(i) for i in input('Введите границу чисел? ').split()]

print(float_number_generation(start, finish))


start, finish = [i for i in input('Введите границу символов? ').split()]

def symbol_generation(start, finish):
    set_str = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
               'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
               'x': 24, 'y': 25, 'z': 26}

    start = set_str[start]
    finish = set_str[finish]
    number_str = str(time.time())
    number_int = time.time()
    generait = number_str.split('.')
    generait = int(generait[1])
    summ = start + finish
    while True:
        generait = generait % summ
        if generait // summ == 0 and generait > finish:
            generait = generait + number_int
        if generait // summ == 0 and generait < start:
            generait = generait + number_int
        if generait >= start and generait <= finish:
            generait = int(generait)
            break

    for k, v in set_str.items():
        if generait == v:
            return k

print(symbol_generation(start, finish))