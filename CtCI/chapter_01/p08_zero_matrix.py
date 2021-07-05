def zero_matrix(matrix):
    M, N = len(matrix), len(matrix[0])
    row, col = set(), set()

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in row:
        matrix[i] = [0] * M

    for j in col:
        for i in range(M):
            matrix[i][j] = 0
    return matrix


matrix = [[0, 2, 0, 4], [5, 6, 7, 0], [9, 10, 11, 12], [13, 14, 15, 16]]
print(zero_matrix(matrix))
