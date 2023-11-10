package algorithm_interview

//https://leetcode.com/problems/valid-palindrome/description/
class ValidPalindrome {
    fun isPalindrome(s: String): Boolean {
        val candidate = s.replace(Regex("[^a-zA-Z0-9]"), "").toLowerCase()
        return candidate == candidate.reversed()
    }
}