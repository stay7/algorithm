/**
 * Example: var ti = TreeNode(5) var v = ti.`val` Definition for a binary tree node. class
 * TreeNode(var `val`: Int) {
 * ```
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * ```
 * }
 */
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    val result = mutableListOf<Int>()

    fun inorderTraversal(root: TreeNode?): List<Int> {
        traverse(root)
        return result
    }

    private fun traverse(node: TreeNode?) {
        if (node == null) return
        traverse(node.left)
        result.add(node.`val`)
        traverse(node.right)
    }
}
