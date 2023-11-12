package algorithm_interview

class ReverseString {
    fun reverseString(s: CharArray): Unit {
        var i = 0
        var j = s.size - 1

        while (i < j) {
            s[i] = s[j].also { s[j] = s[i] }
            i += 1
            j -= 1
        }
    }
}