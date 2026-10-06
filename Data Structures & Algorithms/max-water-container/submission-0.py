class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1
        highest = 0

        while l < r:

            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            highest = max(highest, area)

            if heights[l] < heights[r]:
                l+=1
            elif heights[r] <= heights[l]:
                r-=1
        return highest
