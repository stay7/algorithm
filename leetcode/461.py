"""
2021-07-21
[leetcode](https://leetcode.com/problems/hamming-distance/)
461. Hamming Distance
"""


# Runtime 32 ms (61.65%)
# Memory 14.3 MB (11.53%)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        count = 0
        while result > 0:
            if result % 2 == 1:
                count += 1
            result //= 2
        return count


# Runtime 24 ms (95.37%)
# Memory 14 MB (98.15%)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if "__main__" == __name__:
    print(Solution().hammingDistance(1, 4))
    print(Solution().hammingDistance(3, 1))
