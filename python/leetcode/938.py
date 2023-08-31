"""
2021-04-23
[leetcode](https://leetcode.com/problems/range-sum-of-bst/)
938. Range Sum of BST
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
# Runtime 192 ms (96.58%)
# Memory 22.3 MB (58.95%)
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def search(node: TreeNode):
            if not node:
                return 0
            if node.val < low:
                return search(node.right)
            if node.val > high:
                return search(node.left)
            return node.val + search(node.left) + search(node.right)
        return search(root)


if "__main__" == __name__:
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)),
                    TreeNode(15, right=TreeNode(18)))
    low = 7
    high = 15
    # print(Solution().rangeSumBST(root, low, high))
    root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(
        7, TreeNode(6))), TreeNode(15, TreeNode(13), TreeNode(18)))
    low = 6
    high = 10
    print(Solution().rangeSumBST(root, low, high))
