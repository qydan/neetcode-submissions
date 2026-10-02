class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #base
        if len(strs) == 0 or not strs[0]:
            return ""
        elif len(strs) == 1:
            return strs[0]

        ref = strs[0] #bat
        count = 0
        for i in range(1, len(strs)):
            compare_word = strs[i] #bag
            if len(compare_word) == 0: 
                return ""
            temp = 0
            for j in range(len(compare_word)):
                if j < len(ref) and ref[j] == compare_word[j]: 
                    temp+=1
                else: 
                    break
            if temp == 0: 
                return ""

            if i == 1: 
                count = temp
            else: 
                count = min(count, temp)
        return ref[:count]
