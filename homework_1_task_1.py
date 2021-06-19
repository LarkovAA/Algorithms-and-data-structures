# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите 3-х значное число: ')
composition = 1
the_amount = 0

for num in number:
    num = int(num)
    composition *= num
    the_amount += num

print(f'Произведение = {composition}, сумма = {the_amount}')

