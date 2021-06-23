import cProfile

def sieve_of_eratosthenes(n):
    a = [0] * n # создаем массив с н кол-вом элементов
    for i in range(n):
        a[i] = i

    # вторым эл-ом является единица которую не считают простым и забиваем ее нулем
    a[1] = 0

    m = 2 # замена на 0 начинается с 3-го элемента ( первые два уже нули)
    while m < n: # перебор всех элемиентов до заданного числа
        if a[m] != 0: # если он не равен нулю то
            j = m * 2 # увеличить в два раза ( текущий эл-т простое число)
            while j < n:
                a[j] = 0 # заменить на 0
                j += m # перейти в позицию на m больше
        m += 1

    #print(*a)
    # вывод простых чисел на экран (может быть реализован как угодно)

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    #print(*b)

def sieve_of_eratosthenes_v2(n):
    if n >= 8:
        prime_numbers = [2, 3, 5, 7] # создаем список куда добавляем простые числа
        for i in range(8, n):
            addendum_num = True # пердполагаем что число простое и готовы его добавить
            rezult = [] # список результатов деления
            for g in prime_numbers:
                if i % g == 0: # если элемент делится без отстатка то мы изменяем значение addendum_num на фолсе и добавляем в список результатов и прекращаем цикл
                    addendum_num = False
                    rezult.append(addendum_num)
                    break
                else:
                    addendum_num = True
                    rezult.append(addendum_num)
            if False not in rezult: # если в списке результатов нет фолс то мы добавляем даннное число как простое
                prime_numbers.append(i)
    else:
        prime_numbers = []
        for i in range(n+1):
            if i == 2:
                prime_numbers.append(i)
            if i == 3:
                prime_numbers.append(i)
            if i == 5:
                prime_numbers.append(i)
            if i == 7:
                prime_numbers.append(i)
        #print(*prime_numbers)

for i in 10, 100, 1000, 10000, 100000, 1000000, 10000000:
    print(f'Работа с {i} данными ')
    cProfile.run('sieve_of_eratosthenes(i)')

# Можем сделать вывод что данный алгоритм имеет Линейную сложность Асимптотика O(N) y=0.0005x−6.0225

for i in 10, 100, 1000, 5000, 25000, 50000, 100000, 150000, 200000:
    print(f'Работа с {i} данными ')
    cProfile.run('sieve_of_eratosthenes_v2(i)')

# Можем сделать вывод что от 1000000 данных программа работает вечно. Значит мы имеем сложность квадратичную O(N**2) y=0.0000x2+0.0310x−95.9649 хотя построенное уравнение говорит о линейности
# линейное уравнение y=0.1997x−2247.6893. Получается что все же мой алгоритм имеет линейно\ую сложность