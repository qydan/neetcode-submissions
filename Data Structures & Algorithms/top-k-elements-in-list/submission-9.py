class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequency_map = {}

    for number in nums:
      if number in frequency_map:
        frequency_map[number] += 1
      else:
        frequency_map[number] = 1

    return sorted(frequency_map, key=frequency_map.get)[-k:]
