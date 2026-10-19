class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        unique = set()

        l = 0
        longest = 0

        for r in range(n):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            
            longest = max(longest, r - l + 1)
            unique.add(s[r])
        
        return longest
        