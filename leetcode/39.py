"""
2021-04-05
[leetcode](https://leetcode.com/problems/combination-sum/)
39. Combination Sum
"""

from typing import List


# 15분정도 소요된 것 같다
# Runtime 132 ms (16.45%)
# Memory 14.3 MB (51.18%)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination(n: int, picked: List[int]):
            if n == 0:
                picked.sort()
                if not picked in out:
                    out.append(picked)
                return
            for candidate in candidates:
                if candidate > n:
                    return
                combination(n-candidate, picked + [candidate])

        out = []
        combination(target, [])
        return out


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
        dfs(target, 0, [])
        return result


if "__main__" == __name__:
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    candidates2 = [2, 3, 5]
    target2 = 8
    candidates3 = [2]
    target3 = 1
    candidates4 = [1]
    target4 = 1
    candidates5 = [1]
    target5 = 2
    print(Solution1().combinationSum(candidates1, target1))
    print(Solution().combinationSum(candidates1, target1))
    # print(Solution().combinationSum(candidates3, target3))
    # print(Solution().combinationSum(candidates4, target4))
    # print(Solution().combinationSum(candidates5, target5))
