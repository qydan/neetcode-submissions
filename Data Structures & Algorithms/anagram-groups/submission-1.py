class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for word in strs:
            frequency = [0] * 26
            for char in word:
                    i = ord(char) - ord('a') 
                    frequency[i] += 1
            freq_tuple = tuple(frequency)
        
            if freq_tuple not in group:
                group[freq_tuple] = []
            group[freq_tuple].append(word)

        return list(group.values())