class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums_sorted = sorted(nums)

        n = len(nums)

        for i in range(n):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            target = 0 - nums_sorted[i]
            l = i + 1
            r = n - 1

            while l < r:

                if nums_sorted[l] + nums_sorted[r] < target:
                    l += 1
                elif nums_sorted[l] + nums_sorted[r] > target:
                    r -= 1
                else:
                    res.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
                    l += 1
                    r -= 1
                    while l < r and nums_sorted[l] == nums_sorted[l - 1]:
                        l += 1
                    
                    while l < r and nums_sorted[r] == nums_sorted[r + 1]:
                        r -= 1

    
        return res
        