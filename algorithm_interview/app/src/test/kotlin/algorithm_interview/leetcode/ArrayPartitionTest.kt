package algorithm_interview.leetcode

import kotlin.test.Test
import kotlin.test.assertEquals

class ArrayPartitionTest {
    val dut = ArrayPartition()

    @Test
    fun `1`() {
        val nums = intArrayOf(1, 4, 3, 2)
        assertEquals(4, dut.arrayPairSum(nums))
    }

    @Test
    fun `2`() {
        val nums = intArrayOf(6, 2, 6, 5, 1, 2)
        assertEquals(9, dut.arrayPairSum(nums))
    }
}