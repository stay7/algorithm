"""
2021-04-20
[leetcode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
104. Maximum Depth of Binary Tree
"""


import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 책의 풀이
# BFS로 푸는 방법인데 시간은 같다
# Runtime 44 ms (39.81%)
# Memory 15.3 MB (90.73%)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth


# 트리의 첫 문제
# 입력을 잘못해서 30분 걸렸다
# Runtime 44 ms (39.81%)
# Memory 16.3 MB (17.07%)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def search(parent: TreeNode, level: int):
            l_depth = r_depth = level
            if parent.left:
                l_depth = search(parent.left, level+1)
            if parent.right:
                r_depth = search(parent.right, level+1)
            return max(l_depth, r_depth, level)
        if not root:
            return 0
        return search(root, 1)


if "__main__" == __name__:
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))
    print(Solution().maxDepth(root))
    root = TreeNode(1, right=TreeNode(2))
    print(Solution().maxDepth(root))
    root = None
    print(Solution().maxDepth(root))
    root = TreeNode(0)
    print(Solution().maxDepth(root))
