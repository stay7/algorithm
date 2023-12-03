package algorithm_interview.leetcode

import kotlin.test.Test
import kotlin.test.assertEquals

class ThreeSumTest {
    private val dut = ThreeSum()

    @Test
    fun `1`() {
        val nums = intArrayOf(-1, 0, 1, 2, -1, -4)
        val result = listOf(listOf(-1, -1, 2), listOf(-1, 0, 1))

        assertEquals(result, dut.threeSum(nums))
    }

    @Test
    fun `2`() {
        val nums = intArrayOf(0, 1, 1)
        val result = listOf(emptyList<Int>())

        assertEquals(result, dut.threeSum(nums))
    }

    @Test
    fun `3`() {
        val nums = intArrayOf(0, 0, 0)
        val result = listOf(listOf(0, 0, 0))

        assertEquals(result, dut.threeSum(nums))
    }
}