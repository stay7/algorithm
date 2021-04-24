"""
2021-04-24
[leetcode](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)
783. Minimum Distance Between BST Nodes
"""

import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 중위 순회에 대한 문제였음
# Runtime 24 ms (94.77%)
# Memory 14.2 MB (88.73%)
class Solution:
    def __init__(self) -> None:
        self.result = sys.maxsize
        self.prev = -sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


if "__main__" == __name__:
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    print(Solution().minDiffInBST(root))
    root = TreeNode(90, TreeNode(69, TreeNode(
        49, right=TreeNode(52)), TreeNode(89)))
    print(Solution().minDiffInBST(root))
    root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
    print(Solution().minDiffInBST(root))
