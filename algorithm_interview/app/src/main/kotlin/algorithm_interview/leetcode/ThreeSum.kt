package algorithm_interview.leetcode

// https://leetcode.com/problems/3sum/solutions/266514/my-solution-kotlin/
class ThreeSum {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()

        val result = mutableSetOf<List<Int>>()
        nums.forEachIndexed { index, num ->
            val target = num * -1
            var left = index + 1
            var right = nums.size - 1
            while (left < right) {
                val sum = nums[left] + nums[right]
                when {
                    sum < target -> {
                        left += 1
                    }

                    sum > target -> {
                        right -= 1
                    }

                    else -> {
                        result.add(listOf(num, nums[left], nums[right]))
                        left += 1
                        right -= 1
                    }
                }
            }
        }
        return result.map { it.toList() }
    }
}