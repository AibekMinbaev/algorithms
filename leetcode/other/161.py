class Solution: 

    def equal(self, s, t):
        t_ln, s_ln = len(t), len(s) 
        dif =  abs(t_ln - s_ln)
        if dif > 1 or s == t: 
            return False 

        for i in range(min(t_ln, s_ln)): 
            if s[i] != t[i]: 
                return s[i+1:] == t[i+1:] or s[i+1:] == t[i:] or t[i+1:] == s[i:] 
        return True   # s = "a"  t = ""


s = "aac" 
t = "ab" 
p = Solution() 
print(p.equal(s,t)) 