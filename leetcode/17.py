"""
2021-04-03
[leetcode]()
17. Letter Combinations of a Phone Number
"""


from typing import List


#
# Runtime 28 ms (82.70%)
# Memory 14.1 MB (86.39%)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if index == len(digits):
                out.append(path)
                return

            for char in pad[digits[index]]:
                dfs(index+1, path+char)

        pad = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z'],
               }
        out = []
        if digits == "":
            return []
        dfs(0, "")
        return out


if "__main__" == __name__:
    digits = "23"
    print(Solution().letterCombinations(digits))
    digits1 = ""
    print(Solution().letterCombinations(digits1))
