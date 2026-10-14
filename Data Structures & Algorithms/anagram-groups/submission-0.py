class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        string_by_char_count = {} ## key is an array (tuple) of size 26, value is the string

        for s in strs:
            char_count = 26 * [0]
            for c in s:
                char_count[ord(c.lower()) - ord("a")] += 1
            
            key = tuple(char_count)

            if key in string_by_char_count:
                string_by_char_count[key].append(s)
            else:
                string_by_char_count[key] = [s]
        

        return list(string_by_char_count.values())

            


        