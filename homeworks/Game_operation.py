print('\n == MY GAME ==')

'''
ПОЛЬЗОВАТЕЛЬСКИЙ ВВОД ДАННЫХ:
    base_weap_dmg - урон оружия
    char_class - класс персонажа (1 - воин, 2 - маг, 3 - лунчик)
    char_level - уровень персонажа
    legend_weap - является ли оружие легендарный (да/нет)
    buff - бафф поверх оружия. +X % (10 = +10%)
'''

# == Урон оружия. (Отрицательное не принимаем) == 
while (base_weap_dmg := int(input('Enter base damage: '))) < 0:
    print('Enter base_weap_dmg > 0. Enter correct value')

# == Класс персонажа == 
char_print_dict = {1:'warrior', 2:'magician', 3:'archer', 4:'thief'}
options = ' '.join(f'{k} - {v} \n' for k,v in char_print_dict.items())
while (char_class := int(input(f'Choose your character class:\n {options}'))) not in char_print_dict:
    print('You choosed wrong class! Try again')
print('Your character class is', char_print_dict[char_class])
    
# == Уровень персонажа == 
while not 1 <= (char_level:= int(input('Enter character level: '))) <= 100:
    print('Incorrect char_level. ', end='')

# == Является ли оружие уникальным == 
while (legend_weap := input('Is this weapon legendary? ').lower()) not in ['yes','no']:
    print('Incorrect legendary parameter. ', end='')

# == Бафф к оружию в % == 
while (buff := int(input('Enter buff (%): '))) < 0:
    print('Incorrect buff (%) parameter. ',end='')

# == Общий вес экипировки == 
while (total_equip_weight := float(input('Enter total weight of equipment: '))) < 0:
    print('Incorrect total weight of equipment parameter. ', end='')


'''
РАССЧЕТЫ ВСЕХ ЗНАЧЕНИЙ
'''

# == Классовый коэф. ==
char_class_dict = {1:1.2, 2:1.0, 3:1.1}
total_dmg = base_weap_dmg * char_class_dict[char_class]

# == Уровневый коэф. ==
lvl_bonus = min(char_level, 50)
total_dmg += total_dmg * (lvl_bonus / 100)

# == Прибавка бафа ==
total_dmg += (total_dmg * (buff / 100))

# == Надбавка за легендарность ==
lgnd_dmg = {'yes':0.4, "no":0}
total_dmg += total_dmg * lgnd_dmg[legend_weap]

# == Штраф за перевес ==
weight_dbf = 0
if total_equip_weight > 50:
    weight_dbf = 0.25
    total_dmg -= total_dmg * weight_dbf

'''
ОКОНЧАТЕЛЬНЫЙ ВЫВОД В ТЕРМИНАЛ
'''
total_dmg = round(total_dmg)
print(f"=== Results ===\nClass: {char_class} \n\
Class multiplier: {char_class_dict[char_class]} \n Buff(%): +{buff}\n\
Legendary weapon: {lgnd_dmg[legend_weap] * 100}%\n Overweight: {weight_dbf}%\n\
Total damage: {total_dmg}")