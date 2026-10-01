class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a = sorted(s)
        b = sorted(t)

        return a == b
        # empty_set = {}
        # empty_set = {}
        # for char in s:
        #     empty_set[char] += 1

        # for char in t
        #     empty_set2[char] += 1
