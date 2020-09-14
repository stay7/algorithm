"""
    2020-09-15
    Runtime: 68 ms
    Memory Usage: 14.9 MB
"""

import unittest

class Solution(object):
    def twoSum(self, nums,target):
        indices = sorted(range(len(nums)),key=lambda k:nums[k])
        nums.sort()

        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum > target:
                    break
                if sum == target:
                    return [indices[i],indices[j]]    

        


class TestSolution(unittest.TestCase):
    def test_case1(self):
        nums = [2,7,11,15]
        target = 9
        answer = [0,1]

        self.assertListEqual(Solution().twoSum(nums,target),answer)
        
        
    def test_case2(self):
        nums = [3,2,4]
        target = 6
        answer=[1,2]
        
        self.assertListEqual(Solution().twoSum(nums, target),answer)

    def test_case3(self):
        nums = [3,3]
        target = 6
        answer=[0,1]
        
        self.assertListEqual(Solution().twoSum(nums, target),answer)

if __name__ == "__main__":
    unittest.main()
    