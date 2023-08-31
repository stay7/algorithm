"""
2021-03-31
[leetcode](https://leetcode.com/problems/design-hashmap/)
706. Design HashMap
"""


#
# Runtime 1508 ms (10.05%)
# Memory 40.9 MB (5.20%)
class MyHashMap:

    def __init__(self):
        self.hashmap = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        self.hashmap[key] = -1


if __name__ == "__main__":
    MyHashMap()
