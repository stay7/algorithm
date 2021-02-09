"""
2021-02-07
[leetcode](https://leetcode.com/problems/reorder-data-in-log-files/)
937. Reorder Data in Log Files
"""

from typing import List


# 1. lambda를 이용해 정렬의 우선순위를 정할 수 있는지 몰랐다.
# Runtime 40 ms (42.46%)
# Memory 14.2 MB (88.36%)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitList = []
        letterList = []

        for str in logs:
            list = str.split(' ')
            if list[1].isdigit():
                digitList.append(str)
            else:
                letterList.append(str)
        letterList.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letterList + digitList


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"]
    print(Solution().reorderLogFiles(logs))
    logs1 = ["a1 9 2 3 1", "g1 act car",
             "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(Solution().reorderLogFiles(logs1))
