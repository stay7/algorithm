"""
2021-04-20
[leetcode](https://leetcode.com/problems/invert-binary-tree/)
226. Invert Binary Tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 11분 소요
# linked list swap문제와 거의 동일해서 금방 풀 수 있었다.
# Runtime 32 ms (57.26%)
# Memory 14.2 MB (74.18%)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def swap(node: TreeNode):
            left = right = None
            if node.left:
                left = swap(node.left)
            if node.right:
                right = swap(node.right)
            node.left = right
            node.right = left
            return node
        if root is None:
            return []
        return swap(root)


if "__main__" == __name__:
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    print(Solution().invertTree(root))  # [4,7,2,9,6,3,1]
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().invertTree(root))  # [2,3,1]

    root = None
    print(Solution().invertTree(root))  # []
