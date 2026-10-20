class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        char_count_s1 = 26 * [0]
        char_count_s2 = 26 * [0]

        for i in range(n1):
            char_count_s1[ord(s1[i]) - ord('a')] += 1

            ## adding this here helps check the initial fixed window
            char_count_s2[ord(s2[i]) - ord('a')] += 1 
        
        matches = 0
        for i in range(26):
            if char_count_s1[i] == char_count_s2[i]:
                matches += 1
        
        l = 0

        for r in range(n1, n2): ## we can start at index n1 because we accounted for the intial window
            if matches == 26:
                return True

            r_index = ord(s2[r]) - ord('a')
            char_count_s2[r_index] += 1

            if char_count_s2[r_index] == char_count_s1[r_index]: ## this is from non-matching to matching
                matches += 1
            elif char_count_s2[r_index] == char_count_s1[r_index] + 1: ## this is from matching to non
                matches -= 1
            
            l_index = ord(s2[l]) - ord('a')
            char_count_s2[l_index] -= 1

            if char_count_s2[l_index] == char_count_s1[l_index]: ## this is from non-matching to matching
                matches += 1
            elif char_count_s2[l_index] == char_count_s1[l_index] - 1: ## this is from matching to non
                matches -= 1
            
            l += 1
        
        return matches == 26

            


        

        

        