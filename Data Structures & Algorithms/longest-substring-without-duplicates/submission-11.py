class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        highest = 0
        substring = set()

        while r < len(s):

            # if the substring is shorter then the window (duplicate found)
            if s[r] in substring:
                substring.remove(s[l])
                l += 1
            else:
            # if the substring matches the window
                substring.add(s[r])
                r += 1
                highest = max(highest, len(substring))
        return highest

