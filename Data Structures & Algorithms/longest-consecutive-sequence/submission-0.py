class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = {}

        for n in nums:
            unique[n] = 0 ## 0 mean unvisited, 1 mean visited

        longest_consec = 0
        for n in unique:
            unique[n] = 1
            curr_longest = 1
            if n + 1 not in unique:
                while (n - 1 in unique):
                    unique[n] = 1
                    curr_longest += 1
                    n -= 1

            if curr_longest > longest_consec:
                longest_consec = curr_longest
        
        return longest_consec

        