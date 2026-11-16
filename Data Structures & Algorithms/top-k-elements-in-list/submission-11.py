from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # dictionary of number : frequency
        min_heap = []


        for number, frequency in count.items():
                heapq.heappush(min_heap, (frequency, number))

                if len(min_heap) > k:
                    heapq.heappop(min_heap)

        return [number for frequency, number in min_heap]