class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) -1
        start = 0

        while start < end:
            total = numbers[start] + numbers[end]

            if total == target:
                return [start +1, end+1]

            elif total < target:
                start+=1
            else:
                end-=1
            