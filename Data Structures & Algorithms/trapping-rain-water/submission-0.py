class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointer solution
        if not height: return 0

        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        total_water = 0


        while left < right: 
            if right_max < left_max:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += (right_max - height[right])
            else:
                left +=1
                left_max = max(left_max, height[left])
                total_water += (left_max - height[left])

        return total_water