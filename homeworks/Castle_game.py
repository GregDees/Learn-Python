import random
import time
import sys

def slow_print(text, delay = 0.05):
    for char in  text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
    for _ in range(4):        # 10 циклов анимации
        for i in range(1, 4):  # 1, 2, 3 точки
            print(f'\r{'.' * i}   ', end='', flush=True)
            time.sleep(0.15)
    print('\n')
    time.sleep(1.3)

my_army = 300
my_technic = 200
cas_army = 50
cas_health = 500
turn = 1


# АНИМИРОВАННОЕ НАЧАЛО игры
text = '''Десатник! 
Ты был выбран для командования 
взводом адских десантников во время взятия штурмом 
мегафабрики Автономия на планете Киберстан! 
Гнустные коммунисты автоматоны не должны создать свой аналог 
Демократической космческой станции!
Не подведи Демократию!'''
slow_print(text, 0.02)

print(f'Ваш взвод: {my_army}, Ваша техника: {my_technic}, \nВзвод втоматонов: {cas_army}, Защита мегафабрики: {cas_health}')
while my_army > 0 and cas_health > 0:
    print(f'Раунд: {turn} Выберите действие: \n 1 - Лобовая атака \n 2 - Техника \n 3 - Запросить подкрепление \n 4 - отступить')

    while True:
        action = input('→ ')
        try:
            action = int(action)
        except:
            print('Десантник! Введите верную команду!\n')
            continue
        break

    if action == 1:
        if cas_army > 0:
            cas_health -= random.randrange(20, 40)
            my_army -= round(30 + cas_army / 2)
            cas_army = max(0, cas_army - random.randrange(7, 9))
    elif action == 2:
        if my_technic >= 50:
            cas_health -= 80
            my_technic -= 50
        else:
            turn -= 1
            slow_print(f'Техника закончилась! Вы не можете её применить!\n Раунд: {turn}\n→')
    elif action == 3:
        
        while True:
            sub_action = input('Выберите что хотите восстановить: \n 1 - Взвод \n 2 - Техника\n→ ')
            try:
                sub_action = int(sub_action)
            except:
                print('Десантник! Введите верную команду!\n')
                continue
            break
        
        if sub_action == 1:
            my_army = min(my_army + 50, 300)
            cas_army = min(cas_army + 10, 50)
            slow_print (f'Прибыло подкрепление адского десанта! Взвод пополнен!', 0.02)
        elif sub_action == 2:
            my_technic = min(my_technic + 25, 200)
            cas_army = min(cas_army + 10, 50)
            slow_print (f'Вы запросили подкрепление техникой! Техника пополнена!', 0.02)
        elif sub_action not in range(1,2):
            print('Десантник! Введите верную команду!\n')
    elif action == 4:
        text = '''Вы выбрали отступить!
Какой позор!
Вы будете отправлены под требунал!'''
        slow_print(text, 0.02)
        break

    if my_army <= 0:
        my_army = 0
    print(f'Адские десантники: {my_army}, Техника: {my_technic} Стены мегафабрики: {cas_health}, Автоматоны: {cas_army}')
    turn += 1

if my_army <= 0:
    slow_print('Постыдное поведение! Вы будете отправлены под требунал!', 0.02)
elif cas_health <= 0:
    slow_print('Превосходная доблесть! Демократия вновь восторжествовала! Мы не сомневались в победе!', 0.02)
        