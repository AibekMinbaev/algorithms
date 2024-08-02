#Solution after upsolving: Could not solve during the contest; 
# Time: n 
# Space: 1 
# Topic: Two pointers, sliding window 
# Notes: It turns out that the solution was easy. Don't know why could not solve during the contest. I thought that is is somehow related to backtracking. 
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums) 
        
        res, cnt = 0, 0  
        l, r = 0, 0
        while r < len(nums): 
        
            if nums[r] == mx: 
                cnt += 1  
            
            while cnt >= k: 
                res += len(nums) - r 
                if nums[l] == mx: 
                    cnt -= 1 
                l += 1 
            r += 1
        return res 
                
        