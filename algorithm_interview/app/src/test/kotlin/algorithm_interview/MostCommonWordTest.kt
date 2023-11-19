package algorithm_interview

import org.junit.Test
import kotlin.test.assertEquals

class MostCommonWordTest {
    val dut = MostCommonWord()

    @Test
    fun `1`() {
        val paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        val banned = arrayOf("hit")

        val result = "ball"
        assertEquals(result, dut.mostCommonWord(paragraph, banned))
    }

    @Test
    fun `2`() {
        val paragraph = "a."
        val banned = emptyArray<String>()

        val result = "a"
        assertEquals(result, dut.mostCommonWord(paragraph, banned))
    }

    @Test
    fun `3`() {
        val paragraph = "a, a, a, a, b,b,b,c, c"
        val banned = arrayOf("a")

        val result = "b"
        assertEquals(result, dut.mostCommonWord(paragraph, banned))
    }
}