class Solution: 
    def max_ones_infinite(self, n): 
        res = prev_ones = cur_ones = 0 
        
        for i in range(n): 
            num = int(input()) 
            if num == 1: 
                cur_ones += 1 
            else: 
                prev_ones = cur_ones + 1 
                cur_ones = 0 

            res = max(res, prev_ones + cur_ones)
        return res 

    def max_ones(self, nums): 
        left = zeros = res = 0 
        ln = len(nums) 
        for i in range(ln): 
            if nums[i] == 0: 
                zeros += 1 
                while zeros > 1:
                    if nums[left] == 0: 
                        zeros -= 1 
                    left += 1 
            res = max(res, i - left + 1) 
        return res 
    

# nums = [1, 0, 1, 1, 0, 1, 1]
# s = Solution() 
# print(s.max_ones(nums))  
    
s = Solution() 
print(s.max_ones_infinite(10)) 
