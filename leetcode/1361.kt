"""
2022-08-19
[leetcode](https://leetcode.com/problems/validate-binary-tree-nodes/)
1361. Validate Binary Tree Nodes
"""

class Solution {
    fun validateBinaryTreeNodes(n: Int, leftChild: IntArray, rightChild: IntArray): Boolean {
        val visit = mutableSetOf<Int>()
        var flag = true
        var root = 0
        fun dfs(node: Int) {
            if (node in visit) {
                flag = false
                return
            }
            visit.add(node)
            if (leftChild[node] != -1) dfs(leftChild[node])
            if (rightChild[node] != -1) dfs(rightChild[node])
        }

        fun findRoot(node: Int) {
            root = node
            val indexL = leftChild.indexOf(node)
            if (indexL > 0) return findRoot(indexL)
            val indexR = rightChild.indexOf(node)
            if (indexR > 0) return findRoot(indexR)
        }

        findRoot(0)
        dfs(root)
        return flag && visit.size == n
    }
}
