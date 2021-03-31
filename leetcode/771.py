"""
2021-03-31
[leetcode](https://leetcode.com/problems/jewels-and-stones/)
771. Jewels and Stones
"""


#
# Runtime  24 ms (94.97%)
# Memory 14.3 MB (46.74%)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        for str in stones:
            stone = dict.get(str)
            if stone:
                dict[str] += 1
            else:
                dict[str] = 1

        sum = 0
        for str in jewels:
            jewel = dict.get(str)
            if jewel:
                sum += jewel
        return sum


if __name__ == "__main__":
    jewels = "z"
    stones = "ZZ"
    print(Solution().numJewelsInStones(jewels, stones))
