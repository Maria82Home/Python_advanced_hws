# Number 1
# a, b, c = int(input('first side ')), int(input('second side ')), int(input('third side '))
# if a + b > c and a + c > b and b + c > a:
#     print('yes')
# else:
#     print('no')
# if a == b == c: 
#     print('равносторонний')
# elif a == b or b == c or a == c:
#     print('равобедренный')
# else: 
#     print('разносторонний')

# Number 2
# num = int(input('your number: '))
# f = True
# if num < 0 or num > 100000:
#     print('Wrong input')
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             f = False
#             break
#     print(f) 

# Number 3
from random import randint
MIN = 0
MAX = 1000
num = randint(MIN, MAX)
print(num)
for _ in range(10):    
    mynumber = int(input('guess number: '))
    if mynumber == num:
        print('yes')
        break
    else:
        if mynumber < num: print('it is bigger')
        else: print('it is smaller')


