"""
2022-08-15
[leetcode](https://leetcode.com/problems/diameter-of-binary-tree/)
543. Diameter of Binary Tree
"""
import java.lang.Integer.max

class Solution {
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        var ans = 0
        fun dfs(node: TreeNode?): Int {
            if (node == null) return 0
            val l = dfs(node.left)
            val r = dfs(node.right)
            ans = max(ans, l + r)
            return max(l, r) + 1
        }
        dfs(root)
        return ans
    }
}