"""
2021-04-04
[leetcode](https://leetcode.com/problems/permutations/)
46. Permutations
"""


from typing import List


# python의 객체 참조...
# Runtime 40 ms (67.19%)
# Memory 14.7 MB (15.20%)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(n: int, visited: List[int]):
            visited.append(n)
            if len(visited) == len(nums):
                out.append(visited)
                return
            for w in graph[n]:
                if w not in visited:
                    dfs(w, visited.copy())

        graph = {}
        for num in nums:
            rest = nums.copy()
            rest.remove(num)
            graph[num] = rest

        out = []
        for num in nums:
            visited = []
            dfs(num, visited)

        return out


if "__main__" == __name__:
    nums = [1, 2, 3]
    nums1 = [0, 1]
    nums2 = [1]
    print(Solution().permute(nums))
    print(Solution().permute(nums1))
    print(Solution().permute(nums2))
