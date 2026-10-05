class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = sorted(nums)
        # ==frequency = [0] * len(set(nums))
        group = {}

        for num in nums:
            if num not in group:
                group[num] = 0
            group[num] += 1
        
        arr = []
        for num, count in group.items():
            arr.append([count, num])
        arr.sort()

        #sorted array of count and nums

        return [num for count, num in arr[-k:]]


        