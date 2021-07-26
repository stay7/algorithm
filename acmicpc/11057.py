def sol():
    N = int(input())
    if N == 1:
        return 10
    if N == 2:
        return 55
    unit_nums = list(range(10, 0, -1))
    sum = 55
    for _ in range(N-2):
        prev = unit_nums[0]
        unit_nums[0] = sum
        for i in range(1, 10):
            prev, unit_nums[i] = unit_nums[i], unit_nums[i-1] - prev
            sum += unit_nums[i]
    return sum % 10007


print(sol())
