class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        tlen = len(t)

        if tlen == 0 or tlen > slen:
            return ""
        
        freq_count_t = {}
        freq_count_s = {}

        ## we need to be at least s window length
        for i in range(tlen):
            freq_count_t[t[i]] = freq_count_t.get(t[i], 0) + 1
            freq_count_s[s[i]] = freq_count_s.get(s[i], 0) + 1

        matches = 0
        matches_needed = len(freq_count_t)
        for key in freq_count_t:
            if freq_count_t.get(key) <= freq_count_s.get(key, 0):
                matches += 1
        
        min_window = ""
        curr_window = s[0:tlen]
        l = 0
        for r in range(tlen, slen):

            ## shrink window while valid            
            while matches == matches_needed:
                if len(curr_window) < len(min_window) or min_window == "":
                    min_window = curr_window
                key = s[l]
                freq_count_s[key] -= 1
                curr_window = curr_window[1:]
                ## only care about if it go from match to non-match
                if freq_count_t.get(key, 0) == freq_count_s.get(key) + 1:
                    matches -= 1
                l += 1
            
            key = s[r]
            freq_count_s[key] = freq_count_s.get(key, 0) + 1
            curr_window += s[r]

            ## only care about if it goes from non-match to match
            if freq_count_t.get(key, 0) == freq_count_s.get(key):
                matches += 1

        while matches == matches_needed:
            if min_window == "" or len(curr_window) < len(min_window):
                min_window = curr_window

            key = s[l]
            freq_count_s[key] -= 1
            curr_window = curr_window[1:]

            if freq_count_t.get(key, 0) == freq_count_s[key] + 1:
                matches -= 1

            l += 1
        
        return min_window






        
        
        
        