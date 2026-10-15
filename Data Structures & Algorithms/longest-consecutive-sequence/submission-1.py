class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set(nums)

        longest_consec = 0
        for n in unique:
            curr_longest = 1
            if n + 1 not in unique:
                while (n - 1 in unique):
                    curr_longest += 1
                    n -= 1

            if curr_longest > longest_consec:
                longest_consec = curr_longest
        
        return longest_consec

        