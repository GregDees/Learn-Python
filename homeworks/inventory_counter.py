inventory = [
    {"название": "Меч дракона", "тип": "оружие", "ценность": 7}, # weapon_value = 0 → 7
    {"название": "Старый щит", "тип": "броня", "ценность": 4}, # weapon_value = 7
    {"название": "Зелье здоровья", "тип": "зелье", "ценность": 6}, # 
    {"название": "Лук эльфов", "тип": "оружие", "ценность": 9}, # 
    {"название": "Зелье маны", "тип": "зелье", "ценность": 5} # 
]

# итоговые переменные
item_count, total_worth, weapon_value = (0,) * 3
weapon_name = ''
potion_list = []

for item in inventory:
    # 1. количество предметов в инвентаре
    item_count += 1 
    
    # 2. Подсчет общей ценности
    total_worth += item["ценность"]

    # 3. Самое ценное оружие
    if item["тип"] == "оружие" and item["ценность"] > weapon_value:
        weapon_name = item["название"]
        weapon_value = item["ценность"]

    # 4. Формирование списка зелий
    if item["тип"] == "зелье":
        potion_list.append(item["название"])
    
# РЕЗУЛЬТАТ ПРОГРАММЫ
print('\n\n===================================')
print('Всего предметов: ', item_count) # ✓
print('Общая ценность инвентаря: ', total_worth) # ✓
print(f'Самое ценное оружие: {weapon_name} (ценность = {weapon_value})') # ✓
print('Список зелий: \n', "\n".join(['- ' + x for x in potion_list]), sep = '') # ✓

# users = [
#     {'name':'slava', 'cards':['visa', 'mir pinkoff']},
#     {'name':'iugor', 'cards':['mir pinkoff']},
#     {'name':'bogdan', 'cards':['mir pinkoff']},
#     {'name':'tuflya', 'cards':['visa','mastercard', 'mir pinkoff']}
#  ]

# for user in users:
#     print(user['name'], ': ', end=' ')
#     for card in user['cards']:
#         print(card, end = ', ')
#     print()

# res = ''
# sep = ', '
# for st in a:
#     res += st
#     if st == a[-1]:
#         continue
#     res += sep
# print(res)

# # элем1элем2элем3