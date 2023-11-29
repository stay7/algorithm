package algorithm_interview.leetcode

import algorithm_interview.leetcode.GroupAnagrams
import org.junit.Test
import kotlin.test.assertEquals

class GroupAnagramsTest {
    val dut = GroupAnagrams()

    @Test
    fun `1`() {
        val strs = arrayOf("eat", "tea", "tan", "ate", "nat", "bat")
        val result = listOf(listOf("bat"), listOf("nat", "tan"), listOf("ate", "eat", "tea"))

        assertEquals(result, dut.groupAnagrams2(strs))
    }

    @Test
    fun `2`() {
        val strs = arrayOf("")
        val result = listOf(listOf(""))

        assertEquals(result, dut.groupAnagrams2(strs))
    }

    @Test
    fun `4`() {
        val strs = arrayOf("a")
        val result = listOf(listOf("a"))

        assertEquals(result, dut.groupAnagrams2(strs))
    }
}