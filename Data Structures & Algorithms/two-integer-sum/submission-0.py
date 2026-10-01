class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if (target - nums[i]) == nums[j]:
                    indexes.append(i)
                    indexes.append(j)
                    return indexes