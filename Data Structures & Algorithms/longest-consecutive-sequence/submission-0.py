class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        seen = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 not in seen:
                curr = nums[i]
                length = 1

                while curr+1 in seen:
                    curr+=1
                    length+=1
                
                longest = max(longest, length)

        return longest