#Solution during the contest: Solved 
# Time: n 
# Space: n 
# Topics: Logic, Implementation
# Notes: Just need careful observation to find the solution 

class Solution:
    def minimumAddedCoins(self, c: List[int], t: int) -> int:
        d = Counter(c)   
        res = 0     
        sm = 0
        for i in range(1, t + 1):
            if i in d: 
                sm += i * d[i]
            else: 
                if sm < i: 
                    sm += i
                    res += 1 
        return res    