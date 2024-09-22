# Создайте функцию генератор чисел Фибоначчи

def fibonacci(n: int):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

a = int(input('number '))
print(list(fibonacci(a)))
