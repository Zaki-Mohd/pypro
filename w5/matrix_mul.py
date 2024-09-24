def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Define two matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

result = multiply_matrices(matrix1, matrix2)
print("\nResult of multiplication:")
print(result)