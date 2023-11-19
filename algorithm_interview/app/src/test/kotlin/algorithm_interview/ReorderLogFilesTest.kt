package algorithm_interview

import org.junit.Test
import kotlin.test.assertContentEquals

class ReorderLogFilesTest {

    private val dut = ReorderLogFiles()

    @Test
    fun `1`() {
        val logs = arrayOf("dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero")
        val result = arrayOf("let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6")

        assertContentEquals(result, dut.reorderLogFiles(logs))
    }

    @Test
    fun `2`() {
        val logs = arrayOf("a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo")
        val result = arrayOf("g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7")

        assertContentEquals(result, dut.reorderLogFiles(logs))
    }

    @Test
    fun `3`() {
        val logs = arrayOf("1 n u", "r 527", "j 893", "6 14", "6 82")
        val result = arrayOf("1 n u", "r 527", "j 893", "6 14", "6 82")

        assertContentEquals(result, dut.reorderLogFiles(logs))
    }

    @Test
    fun `4`() {
        val logs = arrayOf("a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car")
        val result = arrayOf("a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7")

        assertContentEquals(result, dut.reorderLogFiles(logs))
    }
}