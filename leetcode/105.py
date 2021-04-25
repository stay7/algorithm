"""
2021-04-25
[leetcode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
105. Construct Binary Tree from Preorder and Inorder Traversal
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# inorder, preorder, postorder 중 2개만 있으면 원본 Tree를 복원할 수 있다.
# Runtime 196 ms (25.76%)
# Memory 88.3 MB (23.07%)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return
        node = TreeNode(preorder[0])
        center = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:center+1], inorder[0:center])
        node.right = self.buildTree(preorder[center+1:], inorder[center+1:])
        return node


if "__main__" == __name__:
    # preorder = [3, 9, 20, 15, 7]
    # inorder = [9, 3, 15, 20, 7]
    # print(Solution().buildTree(preorder, inorder))
    preorder = [1, 2, 4, 7, 3, 5, 6]
    inorder = [4, 7, 2, 1, 5, 3, 6]
    print(Solution().buildTree(preorder, inorder))
