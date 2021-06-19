# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

leap_year = 1764

years = int(input('Введите год который хотите проверить на високосность: '))

check_leap = (years - leap_year) % 4
non_leap_years = [1800, 1900, 2076, 2100]
if check_leap != 0 or years in non_leap_years:
    print('Данный год невисокосный')
else:
    print('Данный год високосный')