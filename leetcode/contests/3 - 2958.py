#Solution after upsolving: 
# Time: n 
# Space: n 
# Topics: Implementation, Logic

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int: 
        res, l = 0, 0  
        d = defaultdict(int) 
        
        for r in range(len(nums)): 
            d[nums[r]] += 1 
            while d[nums[r]] > k: 
                d[nums[l]] -= 1
                l += 1 
            res = max(res, r - l + 1) 
        return res 

#Solution during the contest: Solved
# Time: n 
# Space: n 
# Topics: Implementation

import collections

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int: 
        res = 0 
        l = 0 
        r = 0 
        
        d = collections.defaultdict(int) 
        
        mx_freq = [0]
        cnt = 0 
        
        while r < len(nums): 
            
            d[nums[r]] += 1 
            if mx_freq[-1] < d[nums[r]]: 
                mx_freq.append(d[nums[r]])
            cnt += 1 
            
            if mx_freq[-1] > k: 
                while d[nums[l]] != mx_freq[-1]: 
                    cnt -= 1  
                    d[nums[l]] -= 1
                    l += 1 
                cnt -= 1
                d[nums[l]] -= 1 
                l += 1 

                mx_freq.pop()
            res = max(res, cnt) 
            r += 1 
        return res 