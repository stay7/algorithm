package algorithm_interview.leetcode

class TrappingRainWater {
    // https://leetcode.com/problems/trapping-rain-water/submissions/1109417832/
    fun trap(height: IntArray): Int {
        var sum = 0

        while (true) {
            val leftIdx = height.indexOfFirst { it != 0 }
            val rightIdx = height.indexOfLast { it != 0 }
            if (leftIdx == -1 || rightIdx == -1 || leftIdx == rightIdx) break

            for (i in leftIdx..rightIdx) {
                if (height[i] == 0) {
                    sum += 1
                } else {
                    height[i] -= 1
                }
            }
        }
        return sum
    }

    // https://leetcode.com/problems/trapping-rain-water/submissions/1109432093/
    fun trap2(height: IntArray): Int {
        var sum = 0
        var left = 0
        var right = height.size - 1
        var leftMax = height[left]
        var rightMax = height[right]

        while (left < right) {
            if (leftMax <= rightMax) {
                sum += (leftMax - height[left])
                left += 1
                leftMax = height[left].coerceAtLeast(leftMax)
            } else {
                sum += (rightMax - height[right])
                right -= 1
                rightMax = height[right].coerceAtLeast(rightMax)
            }
        }
        return sum
    }
}