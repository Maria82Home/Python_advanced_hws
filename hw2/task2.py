import math
import fractions

fr1 = input('Введите первую дробь: ')
fr2 = input('Введите вторую дробь: ')
a1 = int(fr1[0])
b1 = int(fr1[2])
a2 = int(fr2[0])
b2 = int(fr2[2])
a_mult = a1 * a2
b_mult = b1 * b2
a_sum = a1 * b2 + a2 * b1
b_sum = b1 * b2


if int(a_sum/math.gcd(a_sum, b_sum)) == int(b_sum/math.gcd(a_sum, b_sum)):
    print('Сумма равна 1')
else:
    print(f'Сумма равна {int(a_sum/math.gcd(a_sum, b_sum))}/{int(b_sum/math.gcd(a_sum, b_sum))}')

if int(a_mult/math.gcd(a_mult, b_mult)) == int(b_mult/math.gcd(a_mult, b_mult)):
    print('Произведение равно 1')
else:
    print(f'Произведение равно {int(a_mult/math.gcd(a_mult, b_mult))}/{int(b_mult/math.gcd(a_mult, b_mult))}')


print('!!!!!!!!Проверка!!!!!!!!!!!!')
a = fractions.Fraction(a1, b1)
b = fractions.Fraction(a2, b2)
print('Сумма равна', a + b)
print('Произведение равно', a * b)

