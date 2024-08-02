#Solution after upsolving: 
# Time and Space same as before
class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:  
        l, r = 1, max(p) 
        res = r 

        while l <= r: 
            k = (l + r)// 2 

            time = 0 
            for elem in p: 
                # time += (elem - 1) // k + 1 
                time += Math.ceil(elem / k) 
            
            if time <= h: 
                res = time 
                r = k - 1 
            else: 
                l = k + 1 
        return res 

#1st Solution 
#Time: n log(max(piles))
#Space: 1 not considering the input array

class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int: 
        l = 1
        r = max(p) 

        while l <= r: 
            m = (l + r)// 2 
            cnt = 0 
            cnt1 = 0 

            for elem in p: 
                cnt += (elem - 1) // m + 1 # why is this working ? 
                cnt1 += (elem - 1) // (m + 1) + 1 
            
            if cnt > h and cnt1 <= h: 
                return m + 1
            elif cnt > h: 
                l = m + 1 
            else: 
                r = m - 1 