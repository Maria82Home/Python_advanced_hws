'''
функция группового переименования файлов.
При переименовании в конце имени добавляется порядковый номер.
Переименование должно работать только для этих файлов внутри каталога.
Переименование происходит для диапазона, например, для [3, 6] берутся буквы
с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
параметры функции слева-направо:
количество цифр в порядковом номере имени файла;
расширение исходное файла;
расширение переименнованного файла;
диапазон имени файла;
желаемое конечное имя файла
'''

import os
from pathlib import Path


def group_rename(count_len: int, extension: str, new_extension: str, interval: list[int], new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.{new_extension}")  #переименование файла по условию

if __name__ == '__main__':
    group_rename(4, 'pip', 'zip', [2, 4], "new")