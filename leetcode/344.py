"""
2021-02-08
[leetcode](https://leetcode.com/problems/reverse-string/)
344. Reverse String
"""


# 1. C언어처럼 푼 문제
# Runtime 188 ms ms (91.03%)
# Memory 18.8 MB (18.82%)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            backIndex = len(s) - 1 - i
            front = s[i]
            s[i] = s[backIndex]
            s[backIndex] = front


# 2. 더 짧게 구현 (시간은 더 오래걸림..!)
# Runtime 256 ms (10.71%)
# Memory 18.8 MB (10.38%)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            left, right = i, len(s) - 1 - i
            s[left], s[right] = s[right], s[left]


# 3. 가장 짧은 구현 (시간은 제일 오래걸림)
# Runtime 296 ms (6.59%)
# Memory 18.7 MB (42.29%)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
