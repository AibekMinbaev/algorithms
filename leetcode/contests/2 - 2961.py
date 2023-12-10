#Solution after upsolving 
# Time: n(logb + logc) # because pow(a,b,c) time complexity is logb
# Space: 1 if not consider result arr 
class Solution:
    def getGoodIndices(self, v: List[List[int]], target: int) -> List[int]: 
        res = []

        for ind, elem in enumerate(v): 
            a, b, c, m = elem # new 
            if pow(pow(a,b,10), c, m) == target: 
                res.append(ind)
        return res 

# # Solution during the contest: Solved 
# # Time: n 
# # Space: 1 if don't consider the res arr 
# # Topic: Implementation 
# # Notes: Since there is no integer overflow in python it is easy to manage. But in java, c++ there might an integer overflow. 

# class Solution:
#     def getGoodIndices(self, v: List[List[int]], target: int) -> List[int]: 
#         res = [] 
        
#         for i in range(len(v)): 
#             a = v[i][0] 
#             b = v[i][1] 
#             c = v[i][2]
#             m = v[i][3]
            
#             if (((a**b) % 10) ** c) % m == target: 
#                 res.append(i) 
#         return res 