"""
2021-07-28
2011. 암호코드
"""


def sol():
    code = input()
    dp = []

    for i, char in enumerate(code):
        count = 0
        if i == 0:
            if char == '0':
                return 0
            units = 1
            prev = char
            dp.append(1)
            continue

        if prev + char >= '10' and prev + char < '27':
            count += units
        if char != '0':
            units = dp[i-1]
            count += dp[i-1]
        prev = char

        if count == 0:
            return 0
        dp.append(count)
    return dp[-1] % 1000000


print(sol())
