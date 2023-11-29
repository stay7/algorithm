package algorithm_interview.leetcode

import algorithm_interview.leetcode.ValidPalindrome
import org.junit.Test
import kotlin.test.assertFalse
import kotlin.test.assertTrue

class ValidPalindromeTest {

    private val dut = ValidPalindrome()

    @Test
    fun `1`() {
        val s = "A man, a plan, a canal: Panama"
        assertTrue { dut.isPalindrome(s) }
    }

    @Test
    fun `2`() {
        val s = "race a car"
        assertFalse { dut.isPalindrome(s) }
    }

    @Test
    fun `3`() {
        val s = " "
        assertTrue { dut.isPalindrome(s) }
    }
    
    @Test
    fun `4`() {
        val s = "0P"
        assertFalse { dut.isPalindrome(s) }
    }
}