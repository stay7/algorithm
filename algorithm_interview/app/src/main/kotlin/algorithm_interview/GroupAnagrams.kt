package algorithm_interview

class GroupAnagrams {
    // https://leetcode.com/problems/group-anagrams/submissions/1102789029/
    fun groupAnagrams(strs: Array<String>): List<List<String>> {

        return strs.map { str ->
            str.groupBy { it } to str
        }.groupBy {
            it.first
        }.mapValues {
            it.value.map { it.second }
        }.map { it.value }
    }

    // https://leetcode.com/problems/group-anagrams/submissions/1102800596/
    // 정렬하면 같은 문자열이 된다
    fun groupAnagrams2(strs: Array<String>): List<List<String>> {
        val dict = mutableMapOf<String, MutableList<String>>()
        strs.forEach { str ->
            dict.compute(str.toCharArray().sorted().joinToString("")) { k, v ->
                if (v == null) {
                    mutableListOf(str)
                } else {
                    v.add(str)
                    v
                }
            }
        }
        return dict.map { it.value }
    }
}