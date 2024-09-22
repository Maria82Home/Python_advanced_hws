# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

list = ['h', 1, 1, 'h', 3, 'h', 3]
result = []
for item in list:
    if list.count(item) > 1 and item not in result:
        result.append(item)
print(result)