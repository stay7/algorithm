package algorithm_interview

import org.junit.Test
import kotlin.test.assertContentEquals

class ReverseStringTest {

    val dut = ReverseString()

    @Test
    fun `1`() {
        val s = charArrayOf('h', 'e', 'l', 'l', 'o')
        dut.reverseString(s)
        assertContentEquals(charArrayOf('o', 'l', 'l', 'e', 'h'), s)
    }

    @Test
    fun `2`() {
        val s = charArrayOf('H', 'a', 'n', 'n', 'a', 'h')
        dut.reverseString(s)
        assertContentEquals(charArrayOf('h', 'a', 'n', 'n', 'a', 'H'), s)
    }

    @Test
    fun `3`() {
        val s = charArrayOf('a')
        dut.reverseString(s)
        assertContentEquals(charArrayOf('a'), s)
    }
}