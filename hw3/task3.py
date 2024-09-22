# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

baggage = {'Спальник': 4, 'Сапоги': 3, 'Вода': 5, 'Куртка': 1, 'Котелок': 1, 'Тушенка': 2,'палатка': 8}
MAX_WEIGHT = 23
take = 0
list_to_take = list()
sorted_result = sorted(baggage, key = baggage.get, reverse=True)
sorted_baggage = {}
for item in sorted_result:
    sorted_baggage[item] = baggage[item]
for key, value in sorted_baggage.items():
    if take + value <= MAX_WEIGHT:
        list_to_take.append(key)
        take += value
print(f'В рюкзак вмещается {MAX_WEIGHT} кг')
print(f'{list_to_take} весят {take} кг')

