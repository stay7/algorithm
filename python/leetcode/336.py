"""
2021-
[leetcode](https://leetcode.com/problems/palindrome-pairs/)
336. Palindrome Pairs
"""

from typing import List

#
# Runtime ms ()
# Memory MB ()


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pass


if "__main__" == __name__:
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(Solution().palindromePairs(words))
    words = ["bat", "tab", "cat"]
    print(Solution().palindromePairs(words))
    words = ["a", ""]
    print(Solution().palindromePairs(words))
