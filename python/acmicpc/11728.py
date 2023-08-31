"""
2021-08-12
11728. 배열 합치기
"""


def merge(A, B):
    out = []
    i = j = 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    if i < len(A):
        out.extend(A[i:])
    else:
        out.extend(B[j:])
    return out


input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
nums = merge(A, B)
print(' '.join(map(str, nums)))
