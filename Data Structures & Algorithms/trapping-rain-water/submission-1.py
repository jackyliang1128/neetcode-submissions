class Solution:
    def trap(self, height: List[int]) -> int:
        ## array to find left highest point
        ## array to find right highest point

        ## each index is (minimum between left and right) - curr height
        n = len(height)

        tallest_left = 0
        left_highest = n * [0]

        for i in range(n):
            left_highest[i] = tallest_left
            tallest_left = max(tallest_left, height[i])
        
        tallest_right = 0
        right_highest = n * [0]

        for i in range(n - 1, -1, -1):
            right_highest[i] = tallest_right
            tallest_right = max(tallest_right, height[i])

        water_amt = 0

        for i in range(n):
            curr_amt = min(left_highest[i], right_highest[i]) - height[i]
            if curr_amt > 0:
                water_amt += curr_amt
    

        return water_amt