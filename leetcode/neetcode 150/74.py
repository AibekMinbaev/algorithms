#Solution after upsolving
#Time: log(n*m) 
#Space: 1 
#Topic: binary search, but only one 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) 
        m = len(matrix[0]) 

        l = 0 
        r = n * m - 1 
        while l <= r: 
            mid = l + (r - l)//2 # this way we can prevent integer overlfow when arr is very large  
            row = mid // m # m is number of rows 
            col = mid % m # leftover will determine the column 
            
            if matrix[row][col] == target: 
                return True 
            elif matrix[row][col] < target: 
                l = mid + 1 
            else: 
                r = mid - 1 
        
        return False 

#1st Solution: 
# Time: logn + logm = log(n*m) 
# Space: m
# Topic: Binary Search. Bad things is that we are using two binary searches 
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         arr = None 

#         l, r = 0, len(matrix) - 1 
#         while l <= r: 
#             m = l + (r - l)//2 

#             if matrix[m][0] <= target and target <= matrix[m][-1]: 
#                 arr = matrix[m] 
#                 break 
#             elif matrix[m][0] > target: 
#                 r = m - 1 
#             else: 
#                 l = m + 1 

#         if arr: 
#             l, r = 0, len(arr) - 1 
#             while l <= r: 
#                 m = l + (r - l) // 2 

#                 if arr[m] == target: 
#                     return True 
#                 elif arr[m] < target: 
#                     l = m + 1 
#                 else: 
#                     r = m - 1 
#         return False  
            
