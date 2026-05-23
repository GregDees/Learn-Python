import random

p_health = 50
g_health = 30
Time = 1

print('Вы встретили в лесу гоблина. У вас 50 здоровья, у гоблина 30 здоровья. Каждый раунд вы выбираете действие')

# НАЧАЛО ИГРЫ
while p_health > 0 and g_health > 0:
    print(f"Ход {Time}. Выберите действие: \n\t1 - атаковать\n\t2 - лечиться \n\t3 - заклинание")
    action = int(input('Ваш выбор: '))

    if action == 1: # атака
        damage = random.randrange(5,16)
        g_health -= damage
        print(f'Вы кусаете гоблина за жопу {damage}!')

    elif action == 2: # лечение
        heal = random.randrange(5,16)
        p_health = min(p_health + heal, 50)
        print(f'Вы излечили жопу на {heal} HP!')

    elif action == 3: # заклинание
        spell = random.randrange(1,5) # 1,2,3,4

        if spell == 1: # лечит игрока на 15 здоровья
            p_health = min(p_health + 15, 50)
            print('Вы излечили жопу на 15 HP!')

        elif spell == 2: # бьёт игрока на 5 здоровья
            p_health -= 5
            print('Вы получили урон по жопе на 5 HP!')

        elif spell == 3: # бьёт гоблина на 8 здоровья
            g_health -= 8
            print('Вы кусаете гоблина за жопу на 8 HP!')

        elif spell == 4: # лечит гоблина на 3 здоровья
            g_health = min(g_health + 3, 30)
            print('Вы случайно излечили жопу гоблина на 3 HP!')

    if g_health > 0:
        dmg = random.randrange(6,12)
        p_health -= dmg
        print(f'Гоблин укусил вас за жопу на {dmg}! \nВаше HP: {p_health} // Гоблина HP: {g_health}')
        Time += 1
    
# ОКОНЧАНИЕ ИГРЫ. Проверка кто победил
if p_health <= 0:
    print('ТВОЯ ЖОПА ПРЕНАДЛЕЖИТ МНЕ')
elif g_health <= 0:
    print('ВЫ УКРАЛИ ЖОПУ ГОБЛИНА')

    