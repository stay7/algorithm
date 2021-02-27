"""
2021-02-25
[leetcode](https://leetcode.com/problems/valid-parentheses/)
20. Valid Parentheses
"""


# Runtime 32 ms(63.62%)
# Memory 14.3 MB(37.93%)
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {}
        bracket_open = ['(', '{', '[']
        bracket_close = [')', '}', ']']
        for i in range(3):
            pair[bracket_open[i]] = bracket_close[i]
            pair[bracket_close[i]] = bracket_open[i]

        stack = []
        strs = list(s)
        for str in strs:
            if str in bracket_open:
                stack.append(str)
                continue

            if len(stack) == 0:
                return False

            key = stack.pop()
            if key != pair[str]:
                return False
        return len(stack) == 0


# str도 iterable하므로 list로 변경 필요 없음
# dictionary에 닫는 괄호만 두는 방법은 list에서 찾는 방법보다 훨씬 효율적
# Runtime 24ms (95.79%)
# Memory 14.3MB (66.49%)
class BetterSolution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in pair:
                stack.append(char)
            elif not stack or pair[char] != stack.pop():
                return False
        return len(stack) == 0


if __name__ == "__main__":
    s = ']'
    print(Solution().isValid(s))
