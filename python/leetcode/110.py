"""
2021-04-21
[leetcode](https://leetcode.com/problems/balanced-binary-tree/)
110. Balanced Binary Tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 조금만 더 집중했으면 10분은 더 줄였을듯! (25분걸림)
# Runtime 48 ms (78.10%)
# Memory 18.9 MB (45.41%)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root: TreeNode):
            if not root:
                return 0
            left = getHeight(root.left)
            right = getHeight(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        return getHeight(root) != -1


if "__main__" == __name__:
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    root = TreeNode(1, TreeNode(2, TreeNode(
        3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    root = TreeNode()
    print(Solution().isBalanced(root))
