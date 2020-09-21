import unittest

"""
2020-09-18
Runtime: 48 ms, faster than 70.47%
Memory Usage: 13.8 MB, less than 58.07%
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I' : 1, 'V': 5, 'X':10, 'L':50, 'C' : 100, 'D':500, 'M':1000}
        romanList = list(s)

        convert = []
        for i,roman in enumerate(romanList):
            convert.append(romanDict[roman])
            if i == 0:
                continue
            if convert[i-1] < convert[i]:
                convert[i-1] = convert[i-1] * -1

        return sum(convert)


class Test_Solution(unittest.TestCase):
    def test_case1(self):
        TC = [("III",3),("IV",4), ("IX",9), ("LVIII",58),("MCMXCIV",1994)]

        for roman,answer in TC:
            self.assertEqual(Solution().romanToInt(roman),answer)


if __name__ == "__main__":
    unittest.main()