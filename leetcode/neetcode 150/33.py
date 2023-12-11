class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r: 
            m = (r + l) //2 

            if nums[m] == target: 
                return m 
            

            elif target < nums[m]: 
                if target >= nums[l] or target < nums[r]: 
                    r = m - 1 

                elif target < nums[l]: 
                    l = m + 1 

            else: 
                if target > nums[r]:  
                    r = m - 1 
                else: 
                    l = m + 1 
        return -1 

        








# # 1st Solution: 
# # Time: 2logn -> logn 
# # Space: 1 
# # Topics: Binary Search, first finding the pivot and then finding the target 
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         def bin_search(arr, l, r, target): 
#             while l <= r: 
#                 m = (l  + r ) // 2 

#                 if arr[m] == target: 
#                     return m 
#                 elif arr[m] < target: 
#                     l = m + 1 
#                 else: 
#                     r = m - 1  
#             return -1 

#         l, r = 0, len(nums) - 1 

#         while l < r: 
#             m = l + (r - l) // 2 

#             if nums[m] > nums[r]: 
#                 l = m + 1 
#             else: 
#                 r = m 
       
#         temp = r
#         if nums[r] <= target and nums[len(nums) - 1] >= target:
#             return bin_search(nums, r, len(nums)-1, target)  
#         else: 
#             if temp != 0: return bin_search(nums, 0, temp - 1, target)
#             return -1


