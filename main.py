import os
import pandas as pd
import sys
import time
import random
print('')
# df = pd.read_csv('C:\\Users\\sahac\\PycharmProjects\\_pandas_teaching\\data\\titanic_kaggle\\train.csv')

# integer - целое a = 2, b = 5_000
# float. a = 5.2 b = 4/3
# decimal - вещественное, точное = FLOAT, но точнее. Decimal('0.54123412313')
# fraction - фракция, дробь # Fraction(1,5)
# complex - комплексное (i) # 5+5j
# boolean - True/False, Правда или Ложь
# set - множество 

from decimal import Decimal
from fractions import Fraction



# int, float, complex, bool, str, list, tuple, range, dict, 
# set, frozenset, bytes, bytearray, memoryview, NoneType, Ellipsis, NotImplementedType, type, object
# Decimal, Fraction, datetime, date, time, timedelta, array, namedtuple, 
# deque, defaultdict, OrderedDict, Counter, ChainMap, Enum, Pattern, Match, UUID, Path, Queue, Lock, Semaphore, Future, Task
# int8, int16, int32, int64, uint8, uint16, uint32, uint64, float16, float32, float64,
# complex64, complex128, bool_, str_, unicode_, datetime64, timedelta64, object_

# 2026-04-30
# ЗАДАЧА №1 .
"""
1. В терминале выводится "введите длину своего члена: "
2. Пользователь вводит десятичное число. К примеру: 16.3
3. Нужно записать число 16.3 в переменную penis_size
4. Вывести в терминал "Размер вашего члена - 16.3 см"
5. На следующей строке округленное значение "Размер члена +- 16 см"
"""
# penis_size = float(input("введите длину своего члена: "))
# print(f"""  Размер вашего члена - {penis_size} 
# Размер члена +- {round(penis_size)} cm""")  # {some_var:.2f}

# ЗАДАЧА №2
"""
1. В терминале выводится "введите месячную зарплату: "
2.  Пользователь вводит зарплату за месяц. К примеру: 50000
        salary = 50000
3. Затем пишем "количество отработанных часов" (из 160 часов стандартных)
5. Пользователь вводит, к примеру: 145
        hours = 145
6. В консоли выводится: 45312.5
"""

# standard_hours = 160
# salary = int(input("введите месячную зарплату: "))
# hours = int(input('Введите сколько работали часов: '))

# actual_salary = salary / standard_hours * hours
# print(f"Зарплата за {hours} часов: {float(actual_salary)} руб.")

# shortage = standard_hours - hours
# print(f"Недоработка: {shortage} часов (норма {standard_hours})")

# avg_normal = salary / standard_hours
# print(f"Средняя за час (по норме): {avg_normal:.2f} руб.")

# avg_actual = actual_salary / standard_hours
# print(f"Средняя за час (фактическая): {avg_actual:.2f} руб.")

# percent_of_norm = hours / standard_hours * 100
# print(f"Отработано {percent_of_norm:.1f}% от нормы")


# yesterday_temp = int(input('температура вчера: '))  # 32
# today_temp = int(input('температура сегодня: ')) # 24


# if today_temp > yesterday_temp:
#     print('сегодня теплее чем вчера')
# elif today_temp < 0:
#     print('братан, ты блять в сибири?')
# elif today_temp < 227:
#     print('алё еблан, ты где такую температуру взял!?')
# elif yesterday_temp == today_temp:
#     print('температуры одинаковые')



# password = input('Enter Password: ')
# correct_password = 'igor_lox'

# while password != correct_password:
#     print('Fuck off')
#     password = input('Enter Password: ')

# print('Access ok')


'''
Программа рассчитывает чистую зарплату (на руки) после налогов, но с учётом:
- Прогрессивной ставки НДФЛ (13% до 5 млн руб. в год, 15% с превышения).
- Социального налогового вычета (если человек платил за обучение/лечение).
- Районного коэффициента (надбавка) для некоторых регионов.

Пользователь вводит:
- Месячную зарплату (до налогов) – например, 200000.
- Регион (цифра): 1 – Москва/СПб (коэф. 1.0), 2 – Север (коэф. 1.5), 3 – Дальний Восток (коэф. 1.2), 4 – Другой (коэф. 1.0).
- Сумма социальных расходов (лечение/учёба) за год (руб). Если нет, вводит 0.
- Наличие инвалидности (да/нет) – если да, то ежемесячный вычет 500 руб (уменьшает налогооблагаемую базу).

Программа должна:
1. Рассчитать годовой доход (месячная × 12).
2. Рассчитать налог по прогрессивной шкале:
    13% с дохода до 5 млн руб.
    15% с суммы превышения (если годовой доход > 5 млн).
3. Применить социальный вычет: уменьшает годовой доход для налога на сумму расходов (но не более 120 000 руб в год).
4. Применить вычет за инвалидность: 500 руб × 12 месяцев (уменьшает налогооблагаемую базу).
5. Вычислить налог к уплате (учитывая вычеты).
6. Начислить районный коэффициент: увеличивает месячную зарплату ДО налога? Нет, обычно коэффициент начисляется на оклад до налога. Сделаем так: районный коэф. увеличивает месячную зарплату (до налога), а налог считается уже с увеличенной суммы.
7. Итоговая чистая зарплата за месяц = (месячная зарплата × районный коэф) − (налог за год / 12).

Вывести подробный отчёт: годовой доход до и после вычетов, налог, чистую месячную зарплату.
'''

'''
1. Назначение
Программа предназначена для расчёта итогового урона одной атаки игрового
персонажа на основе введённых характеристик: базового урона оружия, класса, уровня, 
наличия легендарного оружия, баффа и веса экипировки.
_____________________________________________________________

2. Входные данные (ввод с клавиатуры)
Программа последовательно запрашивает у пользователя:

1. Базовый урон оружия – целое положительное число.
2. Класс персонажа – целое число:
    1 – воин
    2 – маг
    3 – лучник
3. Уровень персонажа – целое число от 1 до 100 включительно (при неверном значении программа завершается с сообщением об ошибке).
4. Легендарное оружие – строка "да" или "нет" (регистр не важен).
5. Бафф (%) – вещественное неотрицательное число, может быть дробным.
6. Общий вес экипировки (кг) – вещественное положительное число.
_____________________________________________________________

3. Логика расчёта (по шагам)

3.1 Множитель класса
    - Воин → множитель 1.2
    - Маг → множитель 1.0
    - Лучник → множитель 1.1

Урон после применения множителя:
    damage = base_damage * class_multiplier

3.2 Бонус за уровень
- Бонус = min(level, 50) (количество процентов, максимум 50%)
- Увеличиваем урон:
    damage = damage + damage * (level_bonus / 100)

3.3 Бафф
- Бафф задаётся в процентах (например, 50 = +50%)
- Увеличиваем урон:
    damage = damage + damage * (buff / 100)

3.4 Легендарное оружие
- Если пользователь ввёл "да", добавляем 40%:
    damage = damage + damage * 0.4
- Если "нет" → без изменений.

3.5 Штраф за перегрузку
- Если weight > 50 кг, урон уменьшается на 25%:
    damage = damage - damage * 0.25

3.6 Округление
Итоговый урон округляется до ближайшего целого числа (по правилам математического округления).
_____________________________________________________________

4. Выходные данные (вывод на экран)

Программа выводит:
- Название класса
- Множитель класса
- Применённый бонус за уровень (в %)
- Введённый бафф (в %)
- Если легендарное оружие – строку "Легендарное оружие: +40%"
- Если перегрузка – строку "Перегрузка: -25%"
- Итоговый урон (целое число)

ПРИМЕР ВЫВОДА:
--- Результат ---
Класс: Воин
Множитель класса: 1.2
Бонус за уровень: +50%
Бафф: +80.0%
Легендарное оружие: +40%
Перегрузка: -25%
Итоговый урон: 189
'''

# юзер вводит размер пениса
# если пенис < 13 см → 'Дядя ваня огурцы корнишоны'
# если пенис > 13 и меньше < 18 → 'Базовичковый размер, дайте у'
# если пенис больше 18 → 'Александр Михайлович, разлогиньтесь'

# a = int(input('введите размер пениса (см): '))
# if a <= 13:
#     print('Дядя ваня огурцы корнишоны')
# elif 13 < a <= 18:
#     print('Базовичковый размер, дайте 2')
# else:
#     print('Александр Михайлович, разлогиньтесь')

# if a == 1:
#     print()



'''
ТЕМА: ЦИКЛЫ. 2026-05-2
'''

# while - пока
# for - цикл


# юзер вводит число от -100 до 100.
    # * добавить проверку на [-100;100)
# в консоль вывести "Вы ввели число: N"
# с помощью while нужно вывести числа от ввел_юзер до 100 
    # * вывести числа в одну строчку (1 / 2 / 3 / 4 ...)

# РЕШЕНИЕ №1. Длинное, человеческое
# i = int(input('Введите число:'))

# while not -100 <= i <= 100:
#     i = int(input('Введите число от -100 до 100:'))

# print('Вы ввели число:', i)

# while i <= 100:
#     print(i, end=' / ')
#     i += 1



# РЕШЕНИЕ №2. Питон момент
# i = int(input('Введите число: '))

# while i != 100:
#     if -100 <= i <= 100:
#         print(i, end=' / ') 
#         i += 1
#     else:
#         i = int(input('Введите число от -100 до 100: '))
# print(i)


# a = 0

# site_allowed = [5,15,20]
# while a < 50:
#     a += 1
#     time.sleep(0.15)
#     if a in site_allowed:
#         print(a, ' - разрешенный сайт. Пользуйтесь :)')
#         continue
#     print('ALERT - сайт хуйня, блокируем ',a)

'''
ТЕМА: ЦИКЛЫ. FOR. 2026-05-09
'''
# напиши через while проверку пароля
# correct_password = "slava_best"
# while input('Введите пароль: ') != correct_password:
#     print('Пароль неверный!')
# print('Пароль верный!')


# с помощью while в консоль числа от 0 до 10 включительно

# def counter():
#     n = int(input('Введите число: '))
#     a = 0
#     while a < n:
#         print(a, end = ', ')
#         a += 1
#     print(n)


# a = int(input('видите чесло: '))
# while a < 100:
#     print(a)
#     a += 1

# cocain_dose = [1, 2, 3, 4, 5, 6, 7, 8] 

# print('\nЦИКЛ FOR')
# for gramm in reversed(cocain_dose):
#     print(f'ЗАНЮХНУЛ {gramm}-й грамм', end = ' |')
#     time.sleep(0.2)
#     print(random.choice(['ооо фкусна машала', 'ищо хочу', 'фхххххх sniff мммм', 'БОЛЬШЕ!!! БОЛЬШЕ!!!', 
#                          'АААААА', 'Дозу Дозочку...', 'Press F']))
    

# a = 10
# for i in reversed(range(a+1)): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     print(i, end = ', ')

# Сколько человек в классе?
# > 4
# for / цикл 4 раза:
    # Как зовут вашего одноклассника?
    # > Имя
# classmates = [Имя1, Имя2, Имя3, Имя4]



# counts = int(input('Сколько человек в классе? '))
# dickheads = []
# for i in range(counts):     
#     name = input('Как зовут вашего одноклассника? ')
#     dickheads.append(name)
    
# print(dickheads)


# for i in range(10):
#     print('*' * i)



# print(igor_list, id(igor_list))
# igor_list[0] = 'S'
# print(igor_list, id(igor_list))

# числа, строчки, tuple, frozenset, → НЕ МЕНЯЮТСЯ, immutable
# списки(массивы(list(листы))), множества (set), словарь (dict) → МЕНЯЮТСЯ, mutable

# print('\nЦИКЛ WHILE')
# while classmates:
#     print(classmates.pop())
    

# for perem in classmates:
#     print(perem)





'''
ТЕМА: ЦИКЛЫ. FOR. 2026-05-12
'''


# ВСЕ изменяемые объекты (т.е нехэшируемые объекты) КЛЮЧАМИ БЫТЬ НЕ МОГУТ.

# мы берём хэш
# Затем превращаем его в адрес памяти с помощью усечения (берем несколько цифр)
# если место занято, то прибавляем к этому адресу i^2 (1^2 + 2^2... 
# + 4 +9 + 16 + 25... пока не найдём свободную ячейку)
# если мест нет или тяжело найти → питон расширяет словарь по памяти. 


# неупорядоченная коллекция пар "ключ: значение"
    # ключ - хэшируется, неизменяемый объект
    # значение - пофиг. Список, число, другой словарь и.т.д

# classmates_chlen_size = {'mulkadar': 'very big piska + ∞' , 'igor': 24, 'slava': 100, 'uzbek': 5}

# for key in classmates_chlen_size:
#     # 1-ая итерация: key = 'mulkadar', classmates['mulkadar'] = 'very big piska + ∞'
#     # 2-ая итерация: key = 'igor', classmates['mulkadar'] = 24
#     print(key, ": ", classmates_chlen_size[key], sep = '')
#     # mulkadar: very big piska + ∞

# for item in items: # for-each. Пробегаем по элементам
#     print(item)

# for index in range(len(items)): # for. Пробегаемся по индексам
#     print(items[index])

# students = {'slava':[5,5,5], 'igor':[2,2,3]}
# # slava: 5.0, igor: 2.33

# import statistics

# for name in students:
#     rate = students[name]

#     # 2-ой вариант через sum
#     # s = sum(rate) / len(rate)
    
#     # 3ий вариант через mean
#     s = statistics.mean(rate)

#     # 1-ый вариант через цикл
#     # for mark in rate:
#     #     s += mark

#     print(name, ': ', s, sep = '')


# a = [10,20,30]

# WHILE 
# ind = 0
# fin = 0
# while ind < len(a):
#     print(a[ind])
#     fin += a[ind]
#     ind += 1
# print(fin, fin / len(a))

# FOR ИНДЕКСОВЫЙ
# fin2 = 0
# coll[ind]
# [2,3,4] [0] = 2
# coll ← [ind] = Дай мне элемент (coll) под номером = ind
# coll[ind] из коллекции (coll) вытяни элемент с позицией (ind)
# []

# for s in range(len(a)): # (0,1,2) ТО ЖЕ САМОЕ что и [0,1,2]
#     fin2 += a[s] #1) fin2 + a[0] = 0 + 10 = 10

# print(fin2, fin2 / len(a))

# FOR EACH
# fin3 = 0

# for s in a:  # s = 10,20,30
#     fin3 += s
# print(fin3, ', ', fin3/len(a), sep = '')

# задача.
# Сколько всего чисел?
# > 5
# Цикл 5 раз:
    # 12
    # 56
    # 1
    # 7
    # 100
# Программа выводит только четные числа
# 12, 56, 100

# n = int(input('Введите количество чисел: '))
# mass = []
# for a in range(n):
#     us_num = int(input('Введите число: '))
#     mass.append(us_num)

# for a in mass:
#     if a % 2 == 0:
#         print(a)



'''
ТЕМА: ЦИКЛЫ. 2026-05-14
'''

# while
    # - есть условие выхода из цикла
    # - количество итераций незивестно
    # - нам нужен бесконечный цикл
    # - 
# for
    # each - по элементам коллекции проходимся
    # индексовый / обычный - проходимся по индексам коллекции или просто N раз

# Бесконечный цикл while
# while True:
#     print(1)

# бесокнечный цикл for
# from itertools import count

# for i in count():
#     if i == 10:
#         break
#     print(i)

# for _ in iter(int, 1):
#     pass

# classmates = ['igor', 'mulkadar', 'slava', 'uzbek'] #

# for ind in range(len(classmates)):
#     if classmates[ind] == 'slava':
#         print(ind+1, ' ← Вы нашли Славу!!!')

# for people in classmates:
#     print(people)


# 10, 9 ... 0
# st =  'slava pidor'
# for a in st[::-1]:
#     print(a)

# чел вводит число. Число → [1,99]
# вывести числа от 0 до этого числа
# value = int(input('Enter your number: '))
# for a in range(value):
#     print(a, end = ', ')
# print(value)


'''
ТЕМА: ЦИКЛЫ. 2026-05-20
'''

# Задача. Сделать массив чисел от -100 до 100
# вывести в консоль все числа через цикл while / for / for-each


# int('2'), str(123), float('1.2'), complex(), bool(2 > 5)
# cheslo = 123456789
# print(list([int(x) for x in str(cheslo)]))

    
# start = -100
# stop = 100
# step = 10
# rng = list(range(start, stop + 1, step)) # range(-100, 101)
# print(rng)


# b = list(range(-100, 101, 1)) # [-100 ... 101]

# for each
# for ind in b:
#     print(ind)

# for индексовый. 0, 1... 201
# for ind in range(len(b)):
#     print(ind, b[ind]) # 0: -100, 1: -99 ... 200: 100

# while индексовый
# 0: -100, 1: -99, 2: -98 ... 199: 99, 200: 100

# a = -100

# while a <= len(b):
#    a += 1
#     print (a, b[a])

# mas = [10,20,30,40,50,60,70,80,90,100]
# # print(mas[::-1])

# b = list(range(100,10, -1))
# print(b)

# for i in reversed(range(100,10,-1)):
#     print(i)

# Big O()
# Big O(n)
# import timeit

# start = timeit.default_timer()

# a = []
# for i in range(1_000_000_0):
#     a.append(i)
#     for j in reversed(a):
#         pass

# end = timeit.default_timer()
# print(f'{end-start} секунд')

# тернирование
# a = frozenset({1,2,3})
# b = frozenset({1,2,3})
# print(a == b, (a, b), (id(a), id(b)), sep = '\n')


'''
 Задача.
 Пользователь вводит ширину, и длину
 Нужно вывести квадрат N x M звездочек

 Пример.
 Ширина: >> 4
 Длина: >> 3

 Вывод:
 * * *
 * * *
 * * * 
 * * *
'''

# def draw(rows = 3, columns = 3, char = '*'):
#     for row in range(rows): # кол-во строк
#         for col in range(columns):# кол-во столбиков
#             print(char, end=' ')
#         print()

# # rows = int(input(f'Введите ширину: '))
# # columns = int(input(f'Введите длину: '))
# rows = 3
# columns = 3
# draw(rows, columns, char = '卐')



'''
ТЕМА: ЦИКЛЫ. 2026-05-23
'''

коллекция = ['slava', 20, 'chlen', [2123,213,1], {'key':'value1'}, (2,46,7)]

# # for each >>> elem
# for элемент in коллекция:
#     print(элемент)

# # for index >>> index: elem
# for индекс in range(len(коллекция)):
#     print(индекс, ':', коллекция[индекс])

# enumerate() - 
# index, value = (0, 'God')

# коллекция = {'slava', 20, 'chlen', (2,46,7)}


# for index, value in enumerate(коллекция):
#     print(index, value) 

# def enumerate_by_slava(collection):
#     idx = 0
#     for elem in collection:
#         idx += 1
#         yield idx, elem
    
# print('\n\n СЛАВИН КРУТОЙ ВЫВОД')
# for index, value in enumerate_by_slava(коллекция):
#     print(index,value)


'''
«Расшифровка послания»

Вы нашли старый свиток, на котором записаны важные слова, но некоторые буквы заменены на символ "?".
Каждое слово в свитке пронумеровано (начиная с 1).

Чтобы прочитать секретное послание, нужно:
    1. Пройтись по всем словам (список строк).
    2. Если в слове есть символ "?", заменить "?" на его порядковый номер в слове.

    
Вход:
    words = [
    "с?оват?",
    "python",
    "за?ифро?ан?",
    "код",
    "?????"
]

✅ ожидаемый результат 
['с1оват6', 'python', 'за2ифро7ан10', 'код', '01234']
'''

# words = [
#     "с?оват?",
#     "python",
#     "за?ифро?ан?",
#     "код",
#     "?????"
# ]

# for index, word in enumerate(words):
#     char = list(word)
#     for ind, val in enumerate(char): # ind = (7, '?')
#         if val == '?':
#             char[ind] = str(ind)
#     words[index] = "".join(char)
# print(words)


# '12313'
# 32345
# 312.3
# 2 + 4j
# Decimal(2,3)
# Fraction(1,3)
# [1,2,3]
# {2,4,1}
# {2:2, 1:1}
# frozenset([1,2,3])
# (1,2,3)



# [1,2, [3,[1],[2,2][0]]] # П×
# {1:'', print:'', print('hello'):''} # П× И×?
# {1,2, enumerate} # П✓ И✓ ALERT
# a = dict({1,2,3})
# print(type(a))
# (1,2,[1,2,{3:3}], dict({})) # П× У


'''
Неизменяемые:
- числа (int, float, complex, bool, decimal, fraction)
- строки
- frozen: set, dict
- tuple
- range, bytes
- синглотоны: None, NE, ...
- datetime
регулярк, енам... 

'''

'''
изменяемые:
- коллекци
- листы, словари, множества 
- bytearray
- deque, counter, orderedict (defaultdict)
'''

'''
ТЕМА: ЦИКЛЫ. 2026-05-
'''