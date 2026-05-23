import random
import time
import sys

def eating_helldivers():
    # Параметры
    MAX_POS = 50  # длина "дороги"
    BEETLE_SPEED = 3  # скорость жука
    MARINE_COUNT = 4  # сколько десантников съесть
    DELAY = 0.08  # задержка между кадрами
    DELAY_MSG = 0.35 # задержка между сообщениями
    HD_EMOJ = '🔫🪖'
    BUG_EMOJ = '🐛'
    # 👷🧑‍🔧🧑‍💼👥👨🪖
    # 🪲🤖🪳🐛🐞🐜



    marines_eaten = 0
    remaining = MARINE_COUNT
    while remaining > 0:
        beetle_pos = 0
        marine_pos = MAX_POS
    
        # Погоня за текущим десантником
        while beetle_pos < marine_pos:
            # Строим строку: дорога из точек, Ж на позиции жука, Д на позиции десантника
            # road = ['░'] * (MAX_POS + 1)
            road = [' '] * (MAX_POS + 1)
            road[beetle_pos] = BUG_EMOJ

            road[marine_pos] = HD_EMOJ
            line = ''.join(road)
    
            # Добавляем счётчик оставшихся
            status = f" [{line}] "#  Осталось десантников: {remaining}  
            sys.stdout.write('\r' + status)
            sys.stdout.flush()
    
            time.sleep(DELAY)
    
            # Жук бежит вперёд
            beetle_pos += BEETLE_SPEED
    
        # ----- Жук догнал -----
        # Анимация поедания
        for _ in range(3):
            sys.stdout.write('\r' + ' ' * 80 + '\r')  # очистка строки
            sys.stdout.write(f'\r   ЖУК ВОНЗАЕТ ЖВАЛЫ! ')
            sys.stdout.flush()
            time.sleep(DELAY_MSG)
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.write(f'\r   ХРУМ-ХРУМ!')
            sys.stdout.flush()
            time.sleep(DELAY_MSG)
    
        remaining -= 1
        if remaining > 0:
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.write(f'\r   СЪЕДЕН!   Бежит за следующим...   ')
            sys.stdout.flush()
            time.sleep(DELAY_MSG)
        else:
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.flush()
    
    # Финальное сообщение
    print("\n\n" + "=" * 50)
    print("ЛОРД УЛЬЯ ТЕБЯ РАСТЕРЗАЛ ЗА ПРОСТУПОК! ДА ЗДРАВСТВУЕТ ДЕМОКРАТИЯ!")
    print("=" * 50)

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

    match action:
        case 1: # лобовая атака
            if cas_army > 0:
                cas_health -= random.randrange(20, 40)
                my_army -= round(30 + cas_army / 2)
                cas_army = max(0, cas_army - random.randrange(7, 9))
        case 2: # техника
            if my_technic >= 50:
                cas_health -= 80
                my_technic -= 50
            else:
                turn -= 1
                slow_print(f'Техника закончилась! Вы не можете её применить!\n Раунд: {turn}\n→')
        case 3: # подкрепление
            while True:
                sub_action = input('Выберите что хотите восстановить: \n 1 - Взвод \n 2 - Техника\n→ ')
                try:
                    sub_action = int(sub_action)
                except:
                    print('Десантник! Введите верную команду!\n')
                    continue
                break
        
            match sub_action:
                case 1:
                    my_army = min(my_army + 50, 300)
                    cas_army = min(cas_army + 10, 50)
                    slow_print (f'Прибыло подкрепление адского десанта! Взвод пополнен!', 0.02)
                case 2:
                    my_technic = min(my_technic + 25, 200)
                    cas_army = min(cas_army + 10, 50)
                    slow_print (f'Вы запросили подкрепление техникой! Техника пополнена!', 0.02)
        case 4: # гадкое позорное отступление, предатель демократии!!!
            text = '''Вы выбрали отступить!
Какой позор!
Вы будете отправлены под трибунал!
Ваш конец очевиден...'''
            slow_print(text, 0.02)
            eating_helldivers()
            break   

    if my_army <= 0:
        my_army = 0
    print(f'Адские десантники: {my_army}, Техника: {my_technic} Стены мегафабрики: {cas_health}, Автоматоны: {cas_army}')
    turn += 1

if my_army <= 0:
    slow_print('Постыдное поведение! Вы будете отправлены под трибунал!', 0.02)
elif cas_health <= 0:
    slow_print('Превосходная доблесть! Демократия вновь восторжествовала! Мы не сомневались в победе!', 0.02)
        