"""
2021-04-01
[leetcode](https://leetcode.com/problems/top-k-frequent-elements/)
347. Top K Frequent Elements
"""

from typing import List
import collections


#
# Runtime 96 ms (86.65%)
# Memory 18.8 MB (29.12%)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        items = []
        for item in hashmap.items():
            items.append(item)

        items.sort(key=lambda item: item[1], reverse=True)
        ret = []
        for i in range(k):
            key, _ = items[i]
            ret.append(key)
        return ret


if "__main__" == __name__:
    nums = [1, 2]
    k = 2
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    print(Solution().topKFrequent(nums, k))
