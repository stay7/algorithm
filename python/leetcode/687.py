"""
2021-04-20
[leetcode](https://leetcode.com/problems/longest-univalue-path/)
687. Longest Univalue Path
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 책 풀이
# Runtime 400 ms (44.45%)
# Memory 18 MB (44.92%)
class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            self.result = max(self.result, left+right)
            return max(left, right)
        dfs(root)
        return self.result


# 50분동안 푼 문제...
# Runtime 320 ms (97.42%)
# Memory 18 MB (65.47%)
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest = 0

        def dfs(node: TreeNode, val: int, count=0):
            num_l = num_r = 0
            if node.left:
                if val == node.left.val:
                    num_l = dfs(node.left, val, count+1) + 1
                else:
                    dfs(node.left, node.left.val)
            if node.right:
                if val == node.right.val:
                    num_r = dfs(node.right, val, count+1) + 1
                else:
                    dfs(node.right, node.right.val)
            if self.longest < num_l + num_r:
                self.longest = num_l + num_r
            return max(num_l, num_r)

        if root == None:
            return 0
        dfs(root, root.val)
        return self.longest


if "__main__" == __name__:
    root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)),
                    TreeNode(5, right=TreeNode(5)))
    print(Solution().longestUnivaluePath(root))
    root = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)),
                    TreeNode(5, TreeNode(5)))
    print(Solution().longestUnivaluePath(root))
    root = TreeNode(1, right=TreeNode(1, TreeNode(
        1, TreeNode(1), TreeNode(1)), TreeNode(1, TreeNode(1))))
    print(Solution().longestUnivaluePath(root))
