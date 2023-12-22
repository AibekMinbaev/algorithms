class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        l, r = 0, 0
        d = defaultdict(int) 
        while r < len(s): 
            d[s[r]] += 1 

            while d[s[r]] > 1: 
                res = max(res, r - l) 
                d[s[l]] -= 1 
                l += 1  
            r += 1 
        return max(res, r - l) 