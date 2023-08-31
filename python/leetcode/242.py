"""
2021-05-06
[leetcode](https://leetcode.com/problems/valid-anagram/)
242. Valid Anagram
"""

import collections


# 더 간단하게 하는 방법 -> 두 문자열을 정렬하고 비교하면 끝
# Runtime 40 ms (87.18%)
# Memory 14.4 MB (76.79%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = collections.defaultdict(int)
        dict_t = collections.defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            dict_s[char_s] += 1
            dict_t[char_t] += 1
        return dict_s == dict_t


if "__main__" == __name__:
    s = "anagram"
    t = "nagaram"
    Solution().isAnagram(s, t)
