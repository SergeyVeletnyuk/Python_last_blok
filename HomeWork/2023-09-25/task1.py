
def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        buffer = []
        for j in range(len(matrix[0])):
            buffer.append(matrix[j][i])
        new_matrix.append(buffer)
    return new_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))
