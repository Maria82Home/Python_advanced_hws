DIV_HEX = 16
HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

num: int = int(input('Введите число: '))
save_num: int = num
result: str = ''
while num > 0:
    sym = HEX[num % DIV_HEX] 
    result = sym + result
    num = num // DIV_HEX

print(result)
print(hex(save_num))
print('0x' + result == hex(save_num))
