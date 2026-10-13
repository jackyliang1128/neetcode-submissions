class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}

        for c in s:
            if c in charCount:
                charCount[c] += 1
            else:
                charCount[c] = 1
        
        for c in t:
            if c in charCount:
                charCount[c] -= 1
                if charCount[c] == 0:
                    del charCount[c]
            else:
                return False
        
        if charCount:
            return False
        
        return True


        