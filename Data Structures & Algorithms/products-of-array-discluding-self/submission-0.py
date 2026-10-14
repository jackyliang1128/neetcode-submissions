class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left = n * [0]
        right = n * [0]

        currProdLeft = 1
        for i in range(n):
            left[i] = currProdLeft
            currProdLeft *= nums[i]
        
        ##[1, 1, 2, 8]

        currProdRight = 1
        for i in range(n - 1, -1, -1):
            right[i] = currProdRight
            currProdRight *= nums[i]
        
        ##[48, 24, 6, 1]

        res = []

        for i in range(n):
            res.append(left[i]*right[i])
        
        return res


        