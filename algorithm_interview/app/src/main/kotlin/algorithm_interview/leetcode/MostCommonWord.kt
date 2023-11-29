package algorithm_interview.leetcode

class MostCommonWord {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        return paragraph
            .lowercase()
            .split("[\\s!?',;.]".toRegex())
            .filterNot { it in banned || it == "" }
            .groupBy { it }
            .maxByOrNull { it.value.size }!!.key
    }
}