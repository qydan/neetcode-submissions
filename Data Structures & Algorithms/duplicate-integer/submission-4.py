class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_set = set()

        for number in nums:
            if number in frequency_set:
                return True
            else:
                frequency_set.add(number)

        return False