"""
2021-02-07
[leetcode](https://leetcode.com/problems/valid-palindrome/)
125. Valid Palindrom
"""


import re


# 최초 풀이
# Runtime 56 ms (32.99%)
# Memory 19.8 MB (8.56%)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # extract lower alphanumeric characters
        alpha_numeric_s = []
        for i in range(len(s)):

            # isalnum()을 사용하면 한 번에 할 수 있음!!
            if s[i].isalpha() or s[i].isnumeric():
                alpha_numeric_s.append(s[i].lower())

        start = 0
        end = len(alpha_numeric_s) - 1
        while start < end:
            if alpha_numeric_s[start] != alpha_numeric_s[end]:
                return False
            start = start + 1
            end = end - 1
        return True


# Regex와 sliding window를 이용한 더 나은 풀이
# Runtime 40 ms	(89.73%)
# Memory 15.5 MB (28.27%)
class RegexSolution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
