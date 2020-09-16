"""
   2020-09-16
   Runtime: 24 ms, faster than 97.04% of Python3 online submissions for Reverse Integer.
   Memory Usage: 13.8 MB, less than 55.07% of Python3 online submissions for Reverse Integer.
"""

import unittest

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        isNegative = x < 0
        if isNegative : 
            x = x*-1
        reverse_str = str(x)[::-1]
        
        if isNegative:
            result = int('-'+reverse_str)
        else : 
            result = int(reverse_str)
        
        if result > MAX_INT or result < MIN_INT:
            return 0
        
        return result
        


class TestSolution(unittest.TestCase):
    def test_case1(self):
        source=123
        answer=321
        self.assertEqual(Solution().reverse(source),answer)
    
    def test_case2(self):
        source=-123
        answer=-321
        self.assertEqual(Solution().reverse(source),answer)

    def test_case3(self):
        source=120
        answer=21
        self.assertEqual(Solution().reverse(source),answer)

    def test_case4(self):
        source=1534236469
        answer=0
        self.assertEqual(Solution().reverse(source),answer)

if __name__ == "__main__":
    unittest.main()
