"""
2020-02-11
[leetcode](https://leetcode.com/problems/group-anagrams/)
49. Group Anagrams
"""
from typing import List
import collections


# 처음에 set()을 사용해서 anagram인지 체크하려고 시도
#  -> word를 했을때 같은 값이면 anagram이라는 것을 알 수 있음
# Runtime 92 ms (88.70%)
# Memory 17.1 MB (92.73%)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for str in strs:
            anagrams[''.join(sorted(str))].append(str)
        return list(anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    answer = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    Solution().groupAnagrams(strs)
