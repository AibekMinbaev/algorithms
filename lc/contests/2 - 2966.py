# Solution during the contest: 
# Time: nlogn
# Space: n because sorted() in python uses extra space 



class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums) 
        res = [] 
         
        for i in range(2, len(nums), 3):
            if nums[i] - nums[i-1] <= k and nums[i] - nums[i-2] <= k and nums[i-1] - nums[i-2] <= k: 
                res.append([nums[i-2], nums[i-1], nums[i]]) 
            else: 
                return []  
        return res 
            
        