# 1st Solution: 
# Time: 1 
# Space: 1 
# Topic: Math: n(n - 1) // 2 

t = input().split() 
n = int(t[0]) 
m = int(t[1]) 

new_n = n - m + 1 
mx = (new_n * (new_n - 1)) // 2 

full = n // m 
left = n % m 
full_count = m - left  
left_count = full + 1  

mn1 = (full * (full - 1)) // 2 * full_count 
mn2 = (left_count * (left_count - 1)) // 2 * left 
mn = mn1 + mn2 

print(mn, mx)
