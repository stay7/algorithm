"""
2021-04-21
[leetcode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/)
297. Serialize and Deserialize Binary Tree
"""

# Definition for a binary tree node.


import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 와 어렵다..
# Runtime 136 ms (45.58%)
# Memory 18.9 MB (56.53%)
class Codec:
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        nodes = []
        while queue:
            cur = queue.popleft()
            nodes.append(str(cur.val))
            if cur.val == 'null':
                continue
            if cur.left:
                queue.append(cur.left)
            else:
                queue.append(TreeNode('null'))
            if cur.right:
                queue.append(cur.right)
            else:
                queue.append(TreeNode('null'))
        return ' '.join(nodes)

    def deserialize(self, data: str) -> TreeNode:
        print(data)
        if not data:
            return []

        datas = collections.deque(data.split())
        datas.appendleft('null')
        root = TreeNode(int(datas[1]))
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if datas[index] != 'null':
                node.left = TreeNode(int(datas[index]))
                queue.append(node.left)
            index += 1

            if datas[index] != 'null':
                node.right = TreeNode(int(datas[index]))
                queue.append(node.right)
            index += 1
        return root


if "__main__" == __name__:
    root = TreeNode(1)

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
