"""
2021-04-22
[leetcode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
108. Convert Sorted Array to Binary Search Tree
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 책의 풀이
# 얘는 slicing으로 넘기는데 속도는 느리지만 메모리 사용이 오히려 적네?
# copy하는게 아닌가 -> 찾아보니 slicing은 copy하는게 아님 reference 값만 변경
# Runtime 64 ms (28.39%)
# Memory 15.6 MB (85.65%)
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node


# 30분 걸리기는 했지만 깔끔하게 한 번에 성공
# 처음에는 list를 copy해서 넘기려고 했지만 메모리 낭비라고 생각해 중간에 start, end index만 전달하는 방식으로 변경
# Runtime 56 ms (85.78%)
# Memory 15.7 MB (60.34%)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeTree(start: int, end: int) -> TreeNode:
            node_num = end - start + 1
            if node_num == 1:
                return TreeNode(nums[start])
            if node_num == 2:
                return TreeNode(nums[end], TreeNode(nums[start]))

            center = start + (end-start) // 2
            node = TreeNode(nums[center])
            node.left = makeTree(start, center-1)
            node.right = makeTree(center+1, end)
            return node
        return makeTree(0, len(nums) - 1)


if "__main__" == __name__:
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(nums))
