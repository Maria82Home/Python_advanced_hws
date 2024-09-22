# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: 
# путь, имя файла, расширение файла.
def string_to_tuple(st: str) -> tuple:
    *path, other = st.split('/')
    way = '/'.join(path)
    name, extention = other.split('.')
    return way, name, extention

print(string_to_tuple('https://gbcdn.mrgcdn.ru/uploads/asset/5503888/attachment/8896eba24ded17b70b91abb8fe93fc58.pdf'))
