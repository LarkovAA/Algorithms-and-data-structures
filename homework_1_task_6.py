# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

set_alphabet = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14
                , 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26
                , 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31, 'ю': 32, 'я': 33}

number = int(input('Введите число букву которую хотите определить ? '))

for k, v in set_alphabet.items():
    if number == v:
        print(f'Является буква {k}')
        break