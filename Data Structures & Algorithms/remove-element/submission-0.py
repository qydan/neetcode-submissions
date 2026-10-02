class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        while val in nums:
            nums.remove(val)
        return len(nums)