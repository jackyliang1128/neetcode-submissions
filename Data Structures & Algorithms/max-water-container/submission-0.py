class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l = 0
        r = len(heights) - 1

        while l < r:

            curr_water_level = min(heights[l], heights[r]) * (r - l)

            max_area = max(max_area, curr_water_level)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area