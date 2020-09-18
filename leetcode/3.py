"""
2020-09-19
Runtime: 72 ms, faster than 48.65%
Memory Usage: 13.7 MB, less than 88.08%
"""

import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        listX = list(str(x))
        while len(listX) > 1:
            if listX[0] != listX[-1]:
                return False
            listX.pop(0)
            listX.pop(-1)

        return True


class TestSolution(unittest.TestCase):
    def test_case1(self):
        num = 121
        self.assertTrue(Solution().isPalindrome(num))

    def test_case2(self):
        num = -121
        answer = False
        self.assertFalse(Solution().isPalindrome(num))

    def test_case3(self):
        num = 10
        answer = False
        self.assertFalse(Solution().isPalindrome(num))


if __name__ == "__main__":
    unittest.main()
