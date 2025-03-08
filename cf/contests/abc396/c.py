n, m = map(int, input().split()) 

b_arr = sorted(list(map(int, input().split())), reverse=True)
w_arr = sorted(list(map(int, input().split())), reverse=True) 

i = 0 
res = 0  
while i < n: 
    if b_arr[i] < 0: 
        break 
    res += b_arr[i] 
    i += 1  


j = 0 
while j < min(i, m): 
    if w_arr[j] < 0: 
        break 
    res += w_arr[j] 
    j += 1 

while i < n and j < m: 
    if w_arr[j] + b_arr[i] > 0: 
        res += w_arr[j] + b_arr[i] 
    i += 1 
    j += 1 

print(res) 





