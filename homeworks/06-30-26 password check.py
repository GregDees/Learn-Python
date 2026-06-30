# 1. Нужно какое-то соответствие? (брат с set)
#   Словарь, dict {k:v}. key:value, других коллекций с соотвествием нет
# 2. Нужна динамическая коллекция с индексами?
#   Список, list [] (брат с tuple)
# 3. Нужна коллекция с уникальными элементами и быстрым доступом?
#   Множество, set {} (брат dict)
# 4. Нужна фиксированная коллекция с НЕуникальными элементами?
#   tuple, кортеж (,) (брат с list)

# свойства пароля
# длина, есть ли заглавная, есть ли строчная, есть ли цифра, есть ли спец. символ !@#$%^&*

'''РЕШЕНИЕ СЛАВЫ через словари и any/all
Сложность O(5*N) = O(N), медленне Игоря, но строчек меньше, проще масштабируется, более читаемый
'''
password = input('Введите пароль: ')

SPEC_CHARS = {'!', '@', '#', '$', '%', '^', '&', '*'}
rate = {
    0:'Але долбоеб, не пиши пробелы',
    1:'Слишком слабый', 
    2:'Слабый', 
    3:'Средний', 
    4:'Надежный', 
    5:'Пиздато, сохранил себе'
    }

while True:   
    checks = { # 123ABCabc@
        'Длина меньше 8 символов': len(password) >= 8, # 'Длина меньше 8 символов': True
        'Нет цифр': any(char.isdigit() for char in password), # 'Нет цифр': True // any([True, True, True, False...)
        'Нет строчных букв': any(char.islower() for char in password), # 'Нет строчных букв': True //any([6 фолсов, True, True, True])
        'Нет заглавных букв': any(char.isupper() for char in password), # 'Нет заглавных букв': True 
        'Нет специальных символов': any(char in SPEC_CHARS for char in password) # 'Нет спец. смволов': True
    }
    print(checks)
    issues = [error for error, boolean in checks.items() if not boolean]
    # ['Длина меньше 8 символов'...]
    mark = sum(checks.values(),0)

    # вывод
    print('Пароль: ', password)
    for issue in issues:
        print('-', issue)

    print('Оценка: ', rate[mark])
    password = str(input('\nВведите пароль: '))


'''РЕШЕНИЕ ИГОРЯ
O(N). Быстрее Славы, хуже читается, сложнее масштабируется
'''

'''
password = input('Введите пароль: ')

SPEC_CHARS = {'!', '@', '#', '$', '%', '^', '&', '*'}
# rate = {
#     1:'Слишком слабый', 
#     2:'Слабый', 
#     3:'Средний', 
#     4:'Надежный', 
#     5:'Пиздато, сохранил себе'
#     }

rate = ['Слишком слабый', 'Слабый', 'Средний', 'Надежный', 'Пиздато, сохранил себе']
while True:   
    ratelevel = 4
    pass_issues = ''
    # perem1, perem2 = False, False.. - возможный апргрейд
    has_char_low = False
    has_char_up = False
    has_char_dig = False
    has_char_spec = False
    for char in password:
        if char.isdigit():
            has_char_dig = True
        if char.islower():
            has_char_low = True
        if char.isupper():
            has_char_up = True
        if char in SPEC_CHARS:
            has_char_spec = True

    print('Пароль: ', password)

    if len(password) < 8:
        pass_issues += '- Пароль короткий\n\t'
        ratelevel -= 1
    if not has_char_dig:
        pass_issues += '- Нет цифр\n\t'
        ratelevel -= 1
    if not has_char_low:
        pass_issues += '- Нет строчных букв\n\t'
        ratelevel -= 1
    if not has_char_up:
        pass_issues += '- Нет заглавных букв\n\t'
        ratelevel -= 1
    if not has_char_spec:
        pass_issues += '- Нет спецсимволов\n\t'
        ratelevel -= 1
    # ratelevel = 5 - pass_issues.count('\t') возможный апгрдейт
    print(pass_issues)

    print('Оценка: ', rate[ratelevel])
    password = str(input('Введите пароль: '))
    
    # 7.5 / 10
    # any - это оператор or между предикатами
    # all - оператор and меджу предикатами



'''