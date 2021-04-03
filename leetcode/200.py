"""
2021-04-03
[leetcode](https://leetcode.com/problems/number-of-islands/)
200. Number of Islands
"""

from typing import List, Tuple


#
# Runtime 152 ms (35.37%)
# Memory 15.5 MB (36.80%)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(w) -> int:
            i, j = w
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0])-1:
                return
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dfs((i-1, j))
            dfs((i+1, j))
            dfs((i, j-1))
            dfs((i, j+1))

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs((i, j))
        return count


if "__main__" == __name__:
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))
    # print(Solution().numIslands(grid1))
