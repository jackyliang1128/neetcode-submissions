class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement = {} #key is compliment, value is index
        n = len(nums)

        for i in range(n):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[target - nums[i]] = i
        


   

        