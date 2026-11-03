class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # initial soln -> look at each unique word use a hashmap to store the count 
        # unordered -> thinking of set
        # frequency map -> store duplicates together

        

        seen_word_map = defaultdict(list)

        for i in range(len(strs)):
            sorted_word=tuple(sorted(strs[i]))
            seen_word_map[sorted_word].append(strs[i])

        return list(seen_word_map.values())
            