package algorithm_interview.leetcode

import org.junit.Test
import kotlin.test.assertEquals

class TrappingRainWaterTest {

    private val dut: TrappingRainWater = TrappingRainWater()

    @Test
    fun `1`() {
        val heights = intArrayOf(0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)
        val result = 6

        assertEquals(result, dut.trap2(heights))
    }

    @Test
    fun `2`() {
        val heights = intArrayOf(4, 2, 0, 3, 2, 5)
        val result = 9

        assertEquals(result, dut.trap2(heights))
    }
}