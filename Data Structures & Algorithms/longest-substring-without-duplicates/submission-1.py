class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = 0
        r = 0
        longest = 0
        n = len(s)

        while r < n:
            if s[r] in unique:
                while (True):
                    unique.remove(s[l])
                    l += 1
                    if (s[l -1]== s[r]):
                        break
            longest = max(longest, r - l + 1)
            unique.add(s[r])
            r += 1

        return longest
    