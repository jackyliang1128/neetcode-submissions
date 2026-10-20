class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequency_count = {}

        n = len(s)
        l = 0
        longest_consec = 0
        max_frequency = 0

        for r in range(n):
            
            if s[r] not in frequency_count:
                frequency_count[s[r]] = 1
            else:
                frequency_count[s[r]] += 1
            
            max_frequency = max(max_frequency, frequency_count[s[r]])

            while (r - l + 1) - max_frequency > k:
                frequency_count[s[l]] -= 1
                l += 1
            
            longest_consec = max(longest_consec,  r - l + 1)
        
        return longest_consec
            

            



        