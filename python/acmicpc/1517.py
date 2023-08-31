"""
2021-08-13
1517. 버블 소트
"""


def merge(A, B):
    global count
    out = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            count += len(A)-i
            j += 1
    if i < len(A):
        out.extend(A[i:])
    else:
        out.extend(B[j:])
    return out


def divide(nums):
    if len(nums) == 1:
        return nums
    center = len(nums)//2
    return merge(divide(nums[0:center]), divide(nums[center:]))


input()
nums = list(map(int, input().split()))
count = 0
divide(nums)
print(count)
