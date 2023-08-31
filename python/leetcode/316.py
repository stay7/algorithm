"""
2021-02-26
[leetcode](https://leetcode.com/problems/remove-duplicate-letters/)
316. Remove Duplicate Letters
"""


import collections
from typing import Collection


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        print(counter)


if __name__ == "__main__":
    s = 'cbacdcbc'
    print(Solution().removeDuplicateLetters(s))
