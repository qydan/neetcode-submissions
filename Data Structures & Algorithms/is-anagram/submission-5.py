class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_map_s = {}
        frequency_map_t = {}

        if len(s) != len(t):
            return False

        for word_s, word_t in zip(s, t):
            if word_s in frequency_map_s:
                frequency_map_s[word_s] += 1
            else:
                frequency_map_s[word_s] = 1
            if word_t in frequency_map_t:
                frequency_map_t[word_t] += 1
            else:
                frequency_map_t[word_t] = 1

        return frequency_map_s == frequency_map_t
            
            

            