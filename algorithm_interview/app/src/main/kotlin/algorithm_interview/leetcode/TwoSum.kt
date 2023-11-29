package algorithm_interview.leetcode

// https://leetcode.com/problems/two-sum/submissions/1108818175
class TwoSum {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val dict = mutableMapOf<Int, Int>()

        nums.forEachIndexed { index, i ->
            if (dict.contains(target - i)) {
                return intArrayOf(dict.getValue(target - i), index)
            }

            dict[i] = index
        }

        // never reached
        return intArrayOf(0, 0)
    }
}