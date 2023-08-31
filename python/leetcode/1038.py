"""
2021-04-22
[leetcode](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)
1038. Binary Search Tree to Greater Sum Tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
# Runtime ms ()
# Memory MB ()
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def sumNode(node: TreeNode, parent=0):
            left = right = 0
            val = node.val + parent
            if node.right:
                right += sumNode(node.right)
            node.val = val+right
            if node.left:
                left = sumNode(node.left, node.val)
            print(node.val, left, right)
            return val+max(left, right)
        sumNode(root)
        return root


if "__main__" == __name__:
    root = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, right=TreeNode(3))),
                    TreeNode(6, TreeNode(5), TreeNode(7, right=TreeNode(8))))
    print(Solution().bstToGst(root))
