class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        count = {}
        occurrence = [[] for _ in range(size + 1)]

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for n in count:
            occurrence[count[n]].append(n)
        
        res = []

        while len(res) < k:
            currFreq = occurrence[size]
            for i in currFreq:
                res.append(i)
            size -= 1

        
        return res







        