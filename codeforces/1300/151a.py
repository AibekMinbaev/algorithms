t = [int(num) for num in input().split()] 

n = t[0] 
k = t[1] 
l = t[2] 
c = t[3] 
d = t[4] 
p = t[5] 
nl = t[6] 
np = t[7] 


print(min( k * l // nl, c * d, p//np)//n) 
