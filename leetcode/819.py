"""
2021-02-10
[leetcode](https://leetcode.com/problems/most-common-word/)
819. Most Common Word
"""


from typing import List
import re

# 1. regex를 잘못해서 실패한 문제
# Runtime 36 ms	 (67.12%)
# Memory 14.4 MB (21.21%)


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        list = re.sub('[^\w]', ' ', paragraph).lower().split()
        dict = {}
        for str in list:
            if str in dict:
                dict[str] = dict[str] + 1
            else:
                dict[str] = 1

        maxKey, maxValue = '', 0
        for key, value in dict.items():
            if key not in banned and maxValue < value:
                maxKey, maxValue = key, value
        return maxKey


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))
