def rotate_matrix1(matrix):
    N = len(matrix)
    rotated = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated[j][N-1-i] = matrix[i][j]
    return rotated


# in-place rotation
def rotate_matrix2(matrix):
    N = len(matrix[0])
    for layer in range(N//2):
        first = layer
        last = N-1-layer
        for i in range(first, last):
            temp = matrix[first][layer+i]

            # top <- left
            matrix[first][layer+i] = matrix[last-i][first]

            # left <- bottom
            matrix[last-i][first] = matrix[last][last - i]

            # bottom <- right
            matrix[last][last-i] = matrix[layer+i][last]

            # right <- temp
            matrix[layer+i][last] = temp
    return matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(rotate_matrix1(matrix))
print(rotate_matrix2(matrix))
