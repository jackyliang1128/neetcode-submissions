class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        char_freq_s1 = 26 * [0]
        char_freq_s2 = 26 * [0]
        
        for i in range(n1):
            char_freq_s1[ord(s1[i]) - ord('a')] += 1
            char_freq_s2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        for i in range(26):
            if char_freq_s1[i] == char_freq_s2[i]:
                matches += 1
        
        l = 0
        for r in range(n1, n2):
            if matches == 26:
                return True
            
            r_i = ord(s2[r]) - ord('a')
            char_freq_s2[r_i] += 1

            ##non matching to matching
            if char_freq_s1[r_i] == char_freq_s2[r_i]:
                matches += 1
            elif char_freq_s1[r_i] + 1 == char_freq_s2[r_i]:  
                ## matching to non matching 
                matches -= 1
            
            l_i = ord(s2[l]) - ord('a')
            char_freq_s2[l_i] -= 1

            ##non matching to matching
            if char_freq_s1[l_i] == char_freq_s2[l_i]:
                matches += 1
            elif char_freq_s1[l_i] - 1 == char_freq_s2[l_i]:
                ## matching to non matching
                matches -= 1

            l += 1
        
        return matches == 26











