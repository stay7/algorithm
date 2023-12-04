package algorithm_interview.leetcode

// https://leetcode.com/problems/array-partition/submissions/1112100405/
class ArrayPartition {
    fun arrayPairSum(nums: IntArray): Int {
        var sum = 0
        nums.sort()
        nums.forEachIndexed { index, i ->
            if (index % 2 == 0) {
                sum += i
            }
        }
        return sum
    }
}