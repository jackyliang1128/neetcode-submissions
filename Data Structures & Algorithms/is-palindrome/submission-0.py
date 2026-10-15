class Solution:
    def isPalindrome(self, s: str) -> bool:


        filtered_s = "".join(c for c in s if c.isalnum())

        l = 0
        r = len(filtered_s) - 1

        while l < r:
            if filtered_s[l].lower() != filtered_s[r].lower():
                return False
            
            l += 1
            r -= 1
        

        return True
        