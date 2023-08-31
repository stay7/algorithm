"""
2021-04-20
[leetcode](https://leetcode.com/problems/diameter-of-binary-tree/)
543. Diameter of Binary Tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
# Runtime 44 ms (66.56%)
# Memory 16.5 MB (24.93%)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longest = 0

        def search(parent: TreeNode):
            left = right = 0
            if parent.left:
                left = search(parent.left) + 1
            if parent.right:
                right = search(parent.right) + 1
            if self.longest < left+right:
                self.longest = left+right
            return max(left, right)
        search(root)
        return self.longest


if "__main__" == __name__:
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(Solution().diameterOfBinaryTree(root))  # 3
    root = TreeNode(1, TreeNode(2))
    print(Solution().diameterOfBinaryTree(root))  # 1
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(Solution().diameterOfBinaryTree(root))  # 2
    root = TreeNode(1, TreeNode(2, TreeNode(
        3), TreeNode(4, right=TreeNode(5))), TreeNode(6))
    print(Solution().diameterOfBinaryTree(root))  # 4
    root = TreeNode(1)
    print(Solution().diameterOfBinaryTree(root))  # 0
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5)),
                                TreeNode(4, right=TreeNode(6))))
    print(Solution().diameterOfBinaryTree(root))  # 4
