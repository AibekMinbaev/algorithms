class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution after upsolving: Using two pointers 
        # Time: n
        # Space: 1 

        l, r = 0, len(height) - 1
        left_max = height[l] 
        right_max = height[r]
        res =  0 

        while l  < r: 
            if left_max < right_max: 
                l += 1 
                res += max(0, left_max - height[l]) 
                left_max = max(left_max, height[l]) 
            else: 
                r -= 1 
                res += max(0, right_max - height[r]) 
                right_max = max(right_max, height[r])
        return res 
        
        # Solution after upsolving: Without two pointers 
        # Time: n
        # Space: 1 

        # mx_left = [] 
        # mx_right = [] 
        # mx_l = 0 
        # mx_r = 0 
        # for h in height: 
        #     mx_left.append(mx_l) 
        #     mx_l = max(mx_l, h) 

        # for h in height[::][::-1]: 
        #     mx_right.append(mx_r) 
        #     mx_r = max(mx_r, h) 
        
        # res = 0 
        # mx_right = mx_right[::][::-1]

        # for i in range(len(height)): 
        #     res += max(min(mx_right[i], mx_left[i]) - height[i], 0)
        # return res

        # My Solution: 
        # Time: n 
        # Space: 1 

        # def helper(height, res): 
        #     while r < len(height): 
        #         if height[r] >= height[l]: 
        #             res += height[l] * (r - l - 1) - block
        #             block = 0  
        #             l = r 
        #         else: 
        #             block += height[r]
        #         r += 1 
            
        #     return [res, l == r-1, l]

        # res, bl, l = helper(height, 0) 
        # if not bl: 
        #     return helper(height[l::][::-1], res)[0]
        # return res