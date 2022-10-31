import random

def get_matrix(m=5, n=3):
    matrix =[[random.randrange(100) for x in range(m)] for y in range(n)]
    return matrix

def transpose_matrix(matrix):
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed
    

array = [get_matrix(2,2) for i in range(10)]
print(array)

t_array = map(transpose_matrix,array)
print(list(t_array))
