class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        start = 0
        mp = {}
        curr_mp = {}

        for c in t:
            mp[c] = mp.get(c,0)+1

        want = len(mp)
        have = 0

        min_len = len(s) + 1
        min_str = ""
        
        for i, c in enumerate(s):
            if c in mp:
                curr_mp[c] = curr_mp.get(c,0)+1
                if curr_mp[c] == mp[c]:
                    have += 1

            while start < len(s) and want == have:
                if i - start + 1 < min_len:
                    min_len = i - start + 1
                    min_str = s[start:i+1]
            
                if s[start] in curr_mp:
                    curr_mp[s[start]] -= 1
                    if curr_mp[s[start]] < mp[s[start]]:
                        have -= 1
        
                start += 1
        return min_str
                
            
