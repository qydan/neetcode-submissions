class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            k = ''.join(sorted(word))
            group.setdefault(k, []).append(word)

        return list(group.values())