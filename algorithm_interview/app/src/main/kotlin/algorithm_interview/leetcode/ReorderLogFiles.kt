package algorithm_interview.leetcode

// https://leetcode.com/problems/reorder-data-in-log-files/submissions/1102190225/ㄴ
class ReorderLogFiles {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        return logs.partition {
            it.split(" ").get(1).any { !it.isDigit() }
        }.let { (letterLogs, digitLogs) ->
            letterLogs.sortedWith { o1, o2 ->
                val compared = o1.substringAfter(" ").compareTo(o2.substringAfter(" "))
                if (compared == 0) {
                    o1.substringBefore(" ").compareTo(o2.substringBefore(" "))
                } else {
                    compared
                }
            } + digitLogs
        }.toTypedArray()
    }
}