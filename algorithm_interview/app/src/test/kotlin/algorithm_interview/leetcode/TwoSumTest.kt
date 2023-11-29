package algorithm_interview.leetcode

import org.junit.Test
import kotlin.test.assertContentEquals

class TwoSumTest {
    private val dut: TwoSum = TwoSum()

    @Test
    fun `1`() {
        val nums = intArrayOf(2, 7, 11, 15)
        val target = 9

        assertContentEquals(intArrayOf(0, 1), dut.twoSum(nums, target))
    }

    @Test
    fun `2`() {
        val nums = intArrayOf(3, 2, 4)
        val target = 6

        assertContentEquals(intArrayOf(1, 2), dut.twoSum(nums, target))
    }

    @Test
    fun `3`() {
        val nums = intArrayOf(3, 3)
        val target = 6

        assertContentEquals(intArrayOf(0, 1), dut.twoSum(nums, target))
    }
}