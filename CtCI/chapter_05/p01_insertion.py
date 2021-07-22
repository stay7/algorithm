def insertion(N, M, i, j):
    left = ~0 << (j+1)
    right = (1 << i) - 1
    mask = left | right
    cleared = N & mask
    moved = M << i
    return(cleared | moved)


N = int('0b1010101', 2)
M = int('0b101', 2)
i = 1
j = 3
print(bin(insertion(N, M, i, j)))
