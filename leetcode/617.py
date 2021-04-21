"""
2021-04-21
[leetcode](https://leetcode.com/problems/merge-two-binary-trees/)
617. Merge Two Binary Trees
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 책의 풀이... 수준 차이를 느낀다
# Runtime 80 ms (89.92%)
# Memory 15.5 MB (47.90%)
class Solution1:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val+root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            return root1 or root2


#
# Runtime 100 ms (12.35%)
# Memory 15.7 MB (11.40%)
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(node1: TreeNode, node2: TreeNode, head: TreeNode):
            if not node1 and not node2:
                return

            if node1:
                head.val += node1.val
            if node2:
                head.val += node2.val

            left1 = left2 = right1 = right2 = None
            if node1:
                left1, right1 = node1.left, node1.right
            if node2:
                left2, right2 = node2.left, node2.right
            if left1 or left2:
                head.left = TreeNode()
                dfs(left1, left2, head.left)
            if right1 or right2:
                head.right = TreeNode()
                dfs(right1, right2, head.right)
        if not root1 and not root2:
            return
        head = TreeNode()
        dfs(root1, root2, head)
        return head


if "__main__" == __name__:
    root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    root2 = TreeNode(2, TreeNode(1, right=TreeNode(4)),
                     TreeNode(3, right=TreeNode(7)))
    Solution().mergeTrees(root1, root2)
    root1 = None
    root2 = None
    Solution().mergeTrees(root1, root2)

    # root1 = [1, 3, 2, 5], root2 = [2, 1, 3, None, 4, None, 7]
    # Solution().mergeTrees(root1, root2)
