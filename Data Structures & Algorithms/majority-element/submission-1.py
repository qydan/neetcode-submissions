class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        middle = len(nums) // 2 # -> gives us the middle index of the array
        nums.sort()


        return nums[middle]