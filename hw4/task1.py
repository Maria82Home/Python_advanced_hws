# Напишите функцию для транспонирования матрицы

def transponation(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]  # структура транспонированной матцы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    for i in range(len(trans_matrix)):
        print(trans_matrix[i])

matrix = [[1, 2, 3, 6],
          [4, 5, 6, 8],
          [7, 8, 9, 9]]
for i in range(len(matrix)):
    print( matrix[i])

transponation(matrix)