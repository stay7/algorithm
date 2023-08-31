"""
2021-04-01
[leetcode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
3. Longest Substring Without Repeating Characters
"""


# 처음에 예외 케이스를 생각하지 못해 실패했지만 생각하고 코딩하기를 성공한 것 같다
# Runtime 60 ms (74.57%)
# Memory 14.2 MB (81.10%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                max_len = max(max_len, len(hashmap))
                collusion = hashmap[s[i]]
                for j in range(start, collusion + 1):
                    del hashmap[s[j]]
                start = collusion + 1
            hashmap[s[i]] = i

        return max(max_len, len(hashmap))


if __name__ == "__main__":
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))
