class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0
        
        left = 0
        min_length = float('inf')
        current_sum = 0

        for right in range(len(nums)):

            current_sum += nums[right]

            while current_sum>= target:
                current_sum -= nums[left]
                min_length = min(min_length, right - left + 1)
                left += 1


        return 0 if min_length == float('inf') else min_length
