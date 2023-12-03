class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Efficient solution: T: n S: 1 Note: We always move the pointer with the lower height, because that low height has not potencial in future 
        #There is no reason to hang onto the pillar of the smallest size in the current range because in the next iteration, the overall width will decrease by one. Thus, a potential greater area will never be reached by hanging onto the smaller pillar, because even if another taller pillar is found by moving the pointer at the taller pillar, the area must always be calculated with the minimum of the two pillars. 

        l = 0 
        r = len(height) - 1 
        res = 0 

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l)) 

            if height[r] <= height[l]: 
                r -= 1 
            else: 
                l += 1 
        return res  


        # #Brute Force solution: T: n^2 S: 1 Note: Will not pass because of TLE 
        # res = 0 

        # for i in range(len(height)): 
        #     for j in range(i + 1, len(height)): 
        #         res = max(res, min(height[i], height[j]) * (j - i))  
        # return res 
        



        